import socket
import time
ports = [21, 22, 23, 25, 80, 110, 139, 443, 445, 3389]
def port_scanner():
	try:
		host = str(input("Host:  "))
		#port = int(input("Port:  "))
		for port in ports:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)
			time.sleep(2)
			if s.connect_ex((host, port)) == 0:
				print(f"Host: {host} | Port {port} | Open")
				s.close()
			else:
				print(f"Host: {host} | Port {port} | Closed")

	except Exception as e:
		print(f"error:  {e}")
port_scanner()
