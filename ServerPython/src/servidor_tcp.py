import socket
try:
    import positioning
except Exception:
    pass

def get_position():
    #positioning.select_module(270526858)
    #pos=positioning.position()['position']
    #ret="latitude=",pos['latitude'], "&longitude=", pos['longitude']
    #return ret
    return "latitude=60.217033666473&longitude=24.878942093007"


HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (str(HOST), int(PORT))
print orig
tcp.bind((str(HOST), int(PORT)))
tcp.listen(1)
print "Server On"
while True:
    con, cliente = tcp.accept()
    print 'Concectado por', cliente
    msg = con.recv(1024);
    tokenizedLine = msg.split();
    print msg
    if tokenizedLine[0]=='GET':
        request_method = tokenizedLine[0];
        request_object = tokenizedLine[1];
        http_version = tokenizedLine[2];
        if request_object.startswith('/'):
            request_object=request_object[1:]
        print request_method
        print request_object
        print http_version
        
        
    con.send(get_position())
    print 'Finalizando conexao do cliente', cliente
    con.close()
