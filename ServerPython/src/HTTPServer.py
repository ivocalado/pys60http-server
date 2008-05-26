from socket import *
class HTTPServer:
    global host, port;
    global serverSocket;
    global rawRequest;
    def __init__(self, host, port):
        self.host = host;
        self.port = port;
    def doGet(self, connection, params):
        pass
    def doPost(self):
        pass
    def __handlerRequest(self, connection, request):
        self.rawRequest = request
        tokenizedLine = request.split();
        if tokenizedLine=='GET':
            request_method = tokenizedLine[0]
            request_object = tokenizedLine[1]
            http_version = tokenizedLine[2];
            if request_object.startswith('/'):
                request_object=request_object[1:]
            objects=request_object.split('?')
            map={'requisition':objects[0]}
            objects=objects[1].split('&')
            for i in objects:
                iObject = i.split('=')
                map[iObject[0]]=iObject[1]
            self.doGet(connection, map)
        
    def startServer(self):
        tcp = socket(AF_INET, SOCK_STREAM)
        orig = (self.host, self.port)
        print orig
        tcp.bind(orig)
        tcp.listen(1)
        print "Server On"
        while True:
            con, cliente = tcp.accept()
            print 'Concectado por', cliente
            request = con.recv(1024)
            self.__handlerRequest(con, request)
            print cliente, msg
            con.send(get_position())
            print 'Finalizando conexao do cliente', cliente
            con.close()