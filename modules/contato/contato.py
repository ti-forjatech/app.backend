from flask import Blueprint, request, jsonify
from modules.mailme.mailme import Custom_mailme

contato_blueprint = Blueprint('contato', __name__, template_folder='templates', url_prefix='/contato')

@contato_blueprint.post('/enviar')
def send_contact():
    data_from_form = request.json
    cMailme = Custom_mailme(data_from_form['email_contact'], data_from_form['email_msg'])
    cMailme.send_mail()
    return jsonify({'success': "ok"})