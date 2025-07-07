#connection library.
import socket
#for time.sleep().
import time
#Command Line args.
import argparse
from colorama import Fore
#color line
def simple_port_scanner():
	try:
#create the object on the "parser".
                blue = Fore.BLUE
                white = Fore.WHITE
                green = Fore.GREEN
                red = Fore.RED
                yellow = Fore.YELLOW
                
                parser = argparse.ArgumentParser(description="port scanner", add_help=False)
                parser.add_argument("--host", type=str, help="define the host")
                parser.add_argument("--port", type=int, nargs="*", help="define the port")

		#args object
                args = parser.parse_args()

                for port in args.port:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(1)
                        time.sleep(2)
                        if s.connect_ex((args.host, port)) == 0:
                                print(f"{white}Host: {yellow}{args.host} {white}| Port: {yellow}{port} {white}| {green}Open")
                                s.close()
                        else:
                                print(f"{white}Host: {yellow}{args.host} {white}| Port: {yellow}{port} {white}| {red}Closed")
	except Exception as e:
		print(f"error:  {e}")
simple_port_scanner()

