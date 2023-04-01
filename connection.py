import pymysql.cursors

class ConnectionManager:
	def __init__(self):
		self.connection = "test"

	def getConnection(self):
		return self.connection