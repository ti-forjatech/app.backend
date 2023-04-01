from flask import Flask
from modules.contato.contato import contato_blueprint
app = Flask(__name__)
app.register_blueprint(contato_blueprint)