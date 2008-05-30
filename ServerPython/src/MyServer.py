from MobileHTTPServer import *
class MyServer(HTTPServer):
    def __init__(self,host, port):
        HTTPServer.__init__(self, host, port)
	
    
    def doGet(self, request, response):
       functionName=request.getProperty("object-requested")
       attributes=request.getProperty("parameters")
       response.println(str(self.callbacks[functionName](attributes)))
	   #attributes=request.getProperty("parameters")
	   #response.println(str(self.__callbacks[functionName](attributes)))
	
        #print params 
        #print connection
        #connection.close()

def MyFunction(attributes):
	return "Ola mundo!!"

def testFunction(attributes):
	#global testFunctionA, testFunctionB
	return 15
def helloWolrd(attributes):
    return "helloworld"

def My(attributes):
    return "pegou!!!"

def joao(attributes):
    return "joao"

def sum(attributes):
    a=attributes['a']
    b=attributes['b']
    return float(a)+float(b)

def Welcome(attributes):
    a=attributes['nome']
    b=attributes['sobrenome']
    return  "Ola " + a+" " +b+ ", como vai?"

def get_position(attributes):
    #positioning.select_module(270526858)
    #pos=positioning.position()['position']
    #ret="latitude=",pos['latitude'], "&longitude=", pos['longitude']
    #return ret
    return "latitude=60.217033666473&longitude=24.878942093007"

server = MyServer('',5004)
server.addCallBack("MyFunction", MyFunction)
server.addCallBack("testFunction", testFunction)
server.addCallBack("helloWorld", helloWolrd)
server.addCallBack("My", My)
server.addCallBack("joao", joao)
server.addCallBack("sum", sum)
server.addCallBack("Welcome", Welcome)
server.addCallBack("get_position", get_position)
server.startServer()
