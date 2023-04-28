import smtplib, ssl, os, datetime
from email.message import EmailMessage
from dotenv import load_dotenv

class Custom_mailme():
    load_dotenv()

    def __init__(self, contact:str, msg:str):
        self.__context = ssl.create_default_context()
        self.__configs = {
            "host": str(os.getenv('MAIL_HOST')),
            "port": int(os.getenv('MAIL_PORT')),
            "sender": str(os.getenv('MAIL_SENDER')),
            "sender_pass": str(os.getenv('MAIL_SENDER_PASS')),
            "receiver1":str(os.getenv('MAIL_RECEIVER1')),
            "receiver2":str(os.getenv('MAIL_RECEIVER2')),
            "contact_from_site":str(contact),
            "msg_from_site":str(msg)
        }


        self.__set_template_text()
        self.__set_template_html()
        self.__construct_mail()

    def get_configs(self)->dict:
        return self.__configs
    
    def __set_template_text(self)->None:
        self.__template_ready = f"""
        Data:{datetime.datetime.now()}
        Email recebido do site.
        Contato:{self.__configs['contact_from_site']}
        MSG:{self.__configs['msg_from_site']}
        """

    def __set_template_html(self)->None:
        self.__template_ready_html = f"""
        <html>
            <body>
                <p>{datetime.datetime.now()}</p>
                <h1>forjaTech</h1>
                <p>Email recebido do site.</p>
                <p>Email do contato: <span>{self.__configs['contact_from_site']}</span></p>
                <p>Mensagem: <span>{self.__configs['msg_from_site']}</span></p>
            </body>
        </html>
        """
    
    def __construct_mail(self)->None:
        if self.__template_ready or self.__template_ready_html:
            self.__mail = EmailMessage()
            self.__mail['From'] = self.__configs['sender']
            self.__mail['To'] = [self.__configs['receiver1'], self.__configs['receiver2']]
            self.__mail['Subject'] = 'ForjaTech - Contato recebido do site'
            self.__mail.set_content(self.__template_ready)
            self.__mail.add_alternative(self.__template_ready_html, subtype='html')
            self.__smtp = smtplib.SMTP_SSL(self.__configs['host'], self.__configs['port'], context=self.__context)
    
    def send_mail(self):
        self.__smtp.login(self.__configs['sender'], self.__configs['sender_pass'])
        self.__smtp.sendmail(self.__configs['sender'], self.__configs['receiver1'], self.__mail.as_string())
        self.__smtp.sendmail(self.__configs['sender'], self.__configs['receiver2'], self.__mail.as_string())
        self.__smtp.quit()
        return True