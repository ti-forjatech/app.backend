class Contato:
    def __init__(self, data, connection):
        self.connection = connection
        self.data_da_postagem = data['data_da_postagem']
        self.nome = data['nome']
        self.email = data['email']
        self.telefone = data['telefone']
        self.mensagem = data['mensagem']
        self.table_name = 'tb_msg_sent'
        self.set_data()

    def set_data(self):
        self.data_to_send = {
            "data_da_postagem": self.data_da_postagem,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "mensagem": self.mensagem,
        }
    
    def getData(self):
        return self.data_to_send

    def createInfraOfContact(self):
        self.createContactTable()

    def dropTableIfExists(self):
        sql = f"DROP TABLE IF EXISTS {self.table_name}"
        self.execute(sql, None)

    def createContactTable(self):
        # self.dropTableIfExists()
        sql = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        data_da_postagem VARCHAR(10) NOT NULL,
        nome TINYTEXT NOT NULL,
        email TINYTEXT NOT NULL,
        telefone CHAR(12) NOT NULL,
        mensagem TEXT NOT NULL
        )"""
        self.execute(sql, None)
        print(self.table_name, "Created!")
    
    def execute(self, sql, values=None):
        if values is not None:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, values)
        else:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

    def send(self):
        with self.connection.cursor() as cursor:
            sql = f'INSERT INTO {self.table_name} (data_da_postagem, nome, email, telefone, mensagem) VALUES (%s, %s, %s, %s, %s)'
            data = (self.data_da_postagem, self.nome, self.email, int(self.telefone), self.mensagem)
            try:
                cursor.execute(sql, data)
                self.connection.commit()
                print("Mensagem registrada!")
                return True
            except Exception as err:
                print("Erro")
                print(err)