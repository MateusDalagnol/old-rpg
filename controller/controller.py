from flask import render_template, request
from model.aventura import criar_personagem
from model.rolagem import rolar_dados

def criar_personagem_controller(nome, classe_str, raca_str, estilo):
    if estilo.lower() == 'classica':
        # Cria o personagem e rola os dados
        valores = rolar_dados(estilo)
        personagem = criar_personagem(nome, classe_str, raca_str, estilo, valores)
        
        habilidades_classe = list(personagem.classe.habilidades.keys()) if isinstance(personagem.classe.habilidades, dict) else personagem.classe.habilidades
        habilidades_raca = personagem.raca.habilidades

        return render_template('personagem.html',
                               nome=personagem.nome,
                               nivel=personagem.nivel,
                               estilo=estilo,
                               classe_nome=classe_str,
                               habilidades_classe=', '.join(habilidades_classe),
                               raca_nome=raca_str,
                               habilidades_raca=', '.join(habilidades_raca),
                               forca=personagem.forca,
                               destreza=personagem.destreza,
                               constituicao=personagem.constituicao,
                               inteligencia=personagem.inteligencia,
                               sabedoria=personagem.sabedoria,
                               carisma=personagem.carisma)
    else:
        valores = rolar_dados(estilo)
        return render_template('distribuir_atributos.html',
                               nome=nome,
                               classe=classe_str,
                               raca=raca_str,
                               estilo=estilo,
                               valores=valores)

def distribuir_atributos_controller():
    nome = request.form['nome']
    classe_str = request.form['classe']
    raca_str = request.form['raca']
    estilo = request.form['estilo']
    
    personagem = criar_personagem(nome, classe_str, raca_str, estilo, None)
    
    personagem.forca = int(request.form['forca'])
    personagem.destreza = int(request.form['destreza'])
    personagem.constituicao = int(request.form['constituicao'])
    personagem.inteligencia = int(request.form['inteligencia'])
    personagem.sabedoria = int(request.form['sabedoria'])
    personagem.carisma = int(request.form['carisma'])

    habilidades_classe = list(personagem.classe.habilidades.keys()) if isinstance(personagem.classe.habilidades, dict) else personagem.classe.habilidades
    habilidades_raca = personagem.raca.habilidades

    return render_template('personagem.html',
                           nome=personagem.nome,
                           nivel=personagem.nivel,
                           estilo=estilo,
                           classe_nome=classe_str,
                           habilidades_classe=', '.join(habilidades_classe),
                           raca_nome=raca_str,
                           habilidades_raca=', '.join(habilidades_raca),
                           forca=personagem.forca,
                           destreza=personagem.destreza,
                           constituicao=personagem.constituicao,
                           inteligencia=personagem.inteligencia,
                           sabedoria=personagem.sabedoria,
                           carisma=personagem.carisma)