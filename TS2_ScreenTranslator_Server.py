import socket
import os

from moduls.Configure import Configure

def get_config():
	conf = {}
	config = Configure('./config.ini')

	conf['port'] = int(config.read('General', 'port'))
	conf['always_print_ip'] = config.read('General', 'always_print_ip')
	conf['print_ip_first_time'] = config.read('General', 'print_ip_first_time')

	return conf

def start(config):
	hostname = socket.gethostname()
	host = socket.gethostbyname(hostname)

	port = config['port']

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	if config['print_ip_first_time'] == '1':
		print(host)

	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		
		os.system('cls')
		if config['always_print_ip'] == '1':
			print(host)

		print(data)

		return_data = '200'
		s.sendto(return_data.encode('utf-8'), addr)
	s.close()

if __name__=='__main__':
	config = get_config()
	start(config)