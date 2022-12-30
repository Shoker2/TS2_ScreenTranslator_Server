import configparser
import json
import os

class Configure:
	def __init__(self, config_path):
		self.config_path = config_path
		self.config = configparser.ConfigParser()

		if not os.path.isfile(self.config_path):
			self.config['General'] = {
				'port': '4000',
				'always_print_ip': '1',
				'print_ip_first_time': '1'
			}

			self.write()
			
		self.config.read(self.config_path, encoding='utf-8')
		
	def read(self, section, key):
		return self.config[section][key]
	
	def update_dictionary(self, section, key, dic):
		_json = json.dumps(dic, ensure_ascii=False)
		self.update(section, key, _json)
	
	def read_dictionary(self, section, key):
		return json.loads(self.read(section, key))
	
	def	update(self, section, key, arg):
		self.config[section][key] = arg
		self.write()

	def write(self):
		with open(self.config_path, 'w+', encoding='utf-8') as configfile:
			self.config.write(configfile)

if __name__ == '__main__':
	config = Configure('./config.ini')