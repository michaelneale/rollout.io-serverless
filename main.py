from flask import escape

import requests


from rox.server.flags.rox_flag import RoxFlag
from rox.server.rox_server import Rox
import time


def current_time():
    return int(round(time.time() * 1000))

def stopwatch(start_time, msg):
    print(msg + ": " + str(current_time() - start_time))    



# 
# Feature flags state is managed and updated live by Rollout
# Treat it as read only in your function. 
# Even though it is setup once - even if your function is invoked "warm", rollout will 
# still ensure the state of the flags represents the current Rollout console config in the background. 
#
class MyContainer:
     def __init__(self):
        self.spankyChat = RoxFlag()
my_container = MyContainer()


#
# Rollout flag setup (called once for a cold start)
#
Rox.register('', my_container)
start = current_time()
#cancel_event = Rox.setup("5c528ffeaf23cf07f9bb3a85").result()
Rox.setup("5c528ffeaf23cf07f9bb3a85")
stopwatch(start, "Setup time")


if (my_container.spankyChat.is_enabled() == True):
    print('ENABLED')
else:    
    print('NOT ENABLED')


#
# Everything until this point is called once during a "cold start" of the function. 
# 
#
def my_function(request):
    """HTTP Cloud Function. Using: http://flask.pocoo.org/docs/1.0/api/#flask.Request

    Rollout setup info: 
        See https://support.rollout.io/reference for details on how to get your app id and api token.

    Google cloud function deploying: 
        gcloud functions deploy my_function --trigger-http --runtime "python37"    

    """

    if (my_container.spankyChat.is_enabled() == True):
        return "ENABLED"
    else:    
        return 'OK'


