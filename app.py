from flask import Flask
from routes.routes import handler_request

app = Flask(__name__)
handler_request(app) 

if __name__ == '__main__':
    app.run(debug=True)
