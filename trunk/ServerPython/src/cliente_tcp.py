import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
print 'Para sair use CTRL+X\n'
tcp.connect(dest)
msg = raw_input()
tcp.send (msg)
msg = tcp.recv(1024)
print "Server>> ", msg
tcp.close()