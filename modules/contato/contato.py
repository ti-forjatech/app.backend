from flask import Blueprint, request
from connection import ConnectionManager
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
            "data_da_postagem":{
                "dia":day,
                "mes":month,
                "ano":year,
            },
            **data_from_form,
        }

        con = ConnectionManager()
        test = con.getConnection()

        return {
            "dados": test
        }