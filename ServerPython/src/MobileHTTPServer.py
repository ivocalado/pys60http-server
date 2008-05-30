from socket import *

class Request:
    def __init__(self, rawCommand, attributes):
        self.__attributes=attributes
        self.__rawCommand = rawCommand
    def getRawCommand(self):
        return self.__rawCommand
    def setAttributes(self, attributes):
        self.__attributes = attributes
    def getAttributes(self):
        return self.__attributes
    def getProperty(self, key):
        return self.__attributes[key]
    def setProperty(self, key, value):
        self.__attributes[key]=value

class Response:
    def __init__(self):
        self.__response=""
    def println(self, message):
        self.__response=self.__response+message+"\r\n"
    def getResponse(self):
        return self.__response
    
    
class HTTPServer:
    def __init__(self, host, port):
        self.host = host;
        self.port = port;
        self.callbacks={}
    
    def doGet(self, request, response):
        pass
    def doPost(self, request, response):
        pass
    
    def __handlerAttributes(self, rawAttributes):
        rawAttributes=rawAttributes[:len(rawAttributes)-2]
        map={}
        for i in rawAttributes:
            map[i[:i.find(':')]]=i[i.find(':')+2:len(i)-1]
        return map
        
    def __handlerRequest(self, connection, rawRequest):
        self._rawRequest = rawRequest
        #print self._rawRequest
        tokenizedLine=self._rawRequest.split('\n')
        requestLine=tokenizedLine[0]
        attributes = self.__handlerAttributes(tokenizedLine[1:])
        tokenizedLine = requestLine.split()
    #print tokenizedLine
        attributes["request-method"]=tokenizedLine[0]
    #print attributes["request-method"]
        attributes["requisition"]=tokenizedLine[1]
        attributes["http-version"]=tokenizedLine[2]
        request_object = attributes["requisition"]
        if request_object.startswith('/'):
            request_object=request_object[1:]
        #print request_object
    #print "passou aqui"
        objects=request_object.split('?')
        #attributes["object-requested"]
        #print objects
        attributes["object-requested"]=objects[0]
        map={}
        if len(objects)>1:
            
                objects=objects[1].split('&')
                #print objects
                for i in objects:
                    iObject = i.split('=')
                    map[iObject[0]]=iObject[1]
    #print map
        attributes["parameters"]=map
        request = Request(self._rawRequest, attributes)
        response = Response()
    #print attributes
        if attributes["request-method"]=='GET':
           self.doGet(request, response)
        elif attributes["request-method"]=='POST':
            self.doPost(resquest, response)
        rsp = response.getResponse()
        print rsp
        #print rsp
        connection.send(rsp)
    #connection.close()
    def startServer(self):
        tcp = socket(AF_INET, SOCK_STREAM)
        orig = (self.host, self.port)
        print orig
        tcp.bind(orig)
        tcp.listen(1)
        print "Server On"
        while True:
            con, cliente = tcp.accept()
            #print 'Concectado por', cliente
            request = con.recv(1024)
            #print request
            try:
               self.__handlerRequest(con, request)
            except Exception:
               con.send('Bad Request Message')
            #con.send('retorno')
            #print 'Finalizando conexao do cliente', cliente
            con.close()
    def addCallBack(self, key, callback):
        self.callbacks[key]=callback
            
