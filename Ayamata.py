#connection library.
import socket
#for time.sleep().
import time
#Command Line args.
import argparse
from colorama import Fore
#color line

top_ports = [20, 21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443]

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
                parser.add_argument("--top_ports", action="store_true")

		#args object
                args = parser.parse_args()

                if args.top_ports:
                        for port in top_ports:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.settimeout(1)
                                time.sleep(2)
                                if s.connect_ex((args.host, port)) == 0:
                                        print(f"{white}Host: {yellow}{args.host} {white}| Port: {yellow}{port} {white}| {green}Open")
                                        s.close()
                                else:
                                        print(f"{white}Host: {yellow}{args.host} {white}| Port: {yellow}{port} {white}| {red}Closed")
                                        
                if args.port:
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

