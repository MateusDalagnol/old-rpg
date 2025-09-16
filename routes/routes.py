from controller.controller import criar_personagem_controller, distribuir_atributos_controller
from flask import request, render_template

def handler_request(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/criar_personagem', methods=['POST'])
    def criar_personagem_route():
        nome = request.form['nome']
        classe_str = request.form['classe']
        raca_str = request.form['raca']
        estilo = request.form['estilo']
        return criar_personagem_controller(nome, classe_str, raca_str, estilo)
    
    @app.route('/distribuir_atributos', methods=['POST'])
    def distribuir_atributos_route():
        return distribuir_atributos_controller()