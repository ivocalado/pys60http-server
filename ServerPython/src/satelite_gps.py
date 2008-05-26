import appuifw, e32, sys
import positioning

sys.stdout = open('c:\\python\\log_output.txt','w')  
sys.stderr = open('c:\\python\\log_error.txt','w')  

app_lock = e32.Ao_lock()

name = None
modules = None
module_id = None

def get_modules():
    print "\n\n***available modules***"
    t.add(u"\n\n***available modules***")
    modules = positioning.modules()
    print 'modules:', modules
    t.add( unicode( "\n\nmodules: " + str(modules) ) )

def get_default_module():
    print "\n\n***default module***"
    t.add(u"\n\n***default module***")
    module_id = positioning.default_module()
    print 'positioning.default_module():', module_id
    t.add( unicode( "\n\npositioning.default_module(): " + str(module_id) ) )

def get_module_info():
    print "\n***detailed module info***"
    t.add(u"\n\n***detailed module info***")
    module_id = 270526858
    #module_id = 270526860
    positioning.select_module(module_id)
    print "module_info(270526858):", positioning.module_info(module_id)
    t.add( unicode( "\n\nmodule_info(270526858): " + str(positioning.module_info(module_id)) ) )

def get_position():
    print "***position info***"
    t.add(u"\n\n***position info***")
    pos = positioning.position()
    print pos
    print ""
    t.add( unicode( "\n\nposition: " + str(pos) ) )

def set_my_requestors():
    #set_requestors(requestors)
    positioning.set_requestors([{"type":"service", "format":"application","data":"test_app"}])
    
def quit():
    app_lock.signal()


appuifw.app.exit_key_handler=quit

t = appuifw.Text()
appuifw.app.body = t

appuifw.app.menu = [(u"Modules", get_modules), (u"Default Module", get_default_module),
                                    (u"Module Info", get_module_info), (u"Get Position", get_position),
                                    (u"Set Requestors", set_my_requestors), (u"Exit", quit)]

app_lock.wait()
