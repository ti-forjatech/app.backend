from models.contato import Contato

class Db_control:
    def __init__(self, connection):
        self.connection = connection

    def prepareContact(self, data):
        return Contato(data, self.connection)