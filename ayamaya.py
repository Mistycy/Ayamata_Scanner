import socket

def port_scanner():
        try:
                host = str(input("Host:  "))
                port = int(input("Port:  "))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                if s.connect_ex((host, port)) == 0:
                        print(f"{host}:  port {port}  open")
                        s.close()
                else:
                        print("port closed")
        except:
                print("erro")

port_scanner()
