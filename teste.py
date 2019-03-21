import time
from datetime import datetime
import influxdb
import json

class InfluxNapp():

	create_db = True
	def __init__(self, create_db, db_name, host, port, user, password):

		self.create_db = create_db
		self.db_name = db_name
		self.host = host
		self.port = port
		self.user = user
		self.password = password

	def db_operations(self, data):

		client = influxdb.InfluxDBClient(self.host, self.port, self.user, self.password, self.db_name)
		if self.create_db == True:
			client.create_database(self.db_name)
		# query = 'select value from cpu_load_short;'
		client.write_points(data) # writing data
		result = client.query('select * from Test') # getting data from the db
		print(result)

if __name__ == '__main__':
	
	json_data = [
		{
			'measurement':'Test',
			'tags':{ # tags are optional, but can help to identify the data
				'Namespace': 'Teste'
			},
			'time':datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), # json files don't support unix time stamp, so we have to convert it
			'fields':{
				'value':'Testes'
			}
		}
	]
	sys_test = InfluxNapp(create_db = True, db_name = 'Test', host = 'localhost', port = 8086, user = 'root', password = 'root')
	sys_test.db_operations(data = json_data)
