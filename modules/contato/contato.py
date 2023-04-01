from flask import Blueprint, request
from connection import ConnectionManager
from db_control import Db_control
import datetime

contato_blueprint = Blueprint('contato', __name__, template_folder='templates', static_folder='static', url_prefix='/contato')

@contato_blueprint.route('/enviar', methods=['POST'])
def send_contact():
    if request.method == 'POST':
        data_from_form = request.json
        day = datetime.datetime.now().strftime('%d')
        month = datetime.datetime.now().strftime('%m')
        year = datetime.datetime.now().strftime('%Y')

        dados = {
            "data_da_postagem":f'{day}/{month}/{year}',
            **data_from_form,
        }

        con = ConnectionManager().getConnection()
        dbc = Db_control(con)
        contato = dbc.prepareContact(dados)
        contato.createInfraOfContact()
        sent = contato.send()

        if sent:
            return {
                "status": "success",
                "msg":"Mensagem registrada com sucesso!",
            }
        else:
            return {
                "status": "fail",
                "msg":"A mensagem não foi registrada."
            }


