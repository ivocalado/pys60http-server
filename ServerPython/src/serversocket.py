import socket
try:
    import positioning
except Exception:
    pass
_connector = None
_running = True
 
_host = '127.0.0.1'
_port = '2501'
_maxClient = 999
 
debug = True
_policyFile = '<?xml version="1.0" encoding="UTF-8"?><cross-domain-policy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.adobe.com/xml/schemas/PolicyFileSocket.xsd"><allow-access-from domain="*" to-ports="*" secure="false" /><site-control permitted-cross-domain-policies="master-only" /></cross-domain-policy>'
 
## Trace debugging messages.
#  @param aString String to be printed.
def printd( aString ):
    if debug:
        print aString
 
_connector = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
_connector.bind ( ( str(_host), int(_port) ) )
_connector.listen ( int(_maxClient) )
_running = True
 
while _running:
  printd('Running on port ' + _port + ' ... ')
  channel, details = _connector.accept()
 
  if _running:
      printd( 'New connection with: ' + str(details) )
      #channel.setblocking( 0 )
      recvData = channel.recv(2000)
 
      if("policy-file-request" in recvData):
         channel.send(_policyFile)
 
      printd( 'host: ' + str(details[0]) )
      printd( 'port: ' + str(details[1]) )
      printd( 'port: ' + str(int(details[1])) )
 
      channel.close()
      
def get_position():
    positioning.select_module(270526858)
    pos=positioning.position()['position']
    ret="latitude=",pos['latitude'], "&longitude=", pos['longitude']
    return ret


    
    