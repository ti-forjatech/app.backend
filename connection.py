import pymysql.cursors
from configparser import ConfigParser

class ConnectionManager:
	def __init__(self):
		config_object = ConfigParser()
		config_object.read("config.ini")
		dbinfo = config_object['DBINFO']

		self.connection = pymysql.connect(
			host=dbinfo['host'], 
			user=dbinfo['user'],
			password=dbinfo['password'],
			database=dbinfo['database'],
			cursorclass=pymysql.cursors.DictCursor
		)

	def getConnection(self):
		return self.connection