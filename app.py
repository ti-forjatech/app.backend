from flask import Flask
from modules.contato.contato import contato_blueprint
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/contato/enviar":{"origins":"*"}})

app.register_blueprint(contato_blueprint)