from flask import escape

import requests


from rox.server.flags.rox_flag import RoxFlag
from rox.server.rox_server import Rox
import time



class MyContainer:
     def __init__(self):
        self.spankyChat = RoxFlag()

my_container = MyContainer()
print("Registering "+  str(int(round(time.time() * 1000))))

Rox.register('', my_container)
print("Registered "+  str(int(round(time.time() * 1000))))
print("Calling setup "+  str(int(round(time.time() * 1000))))

start = int(round(time.time() * 1000))
cancel_event = Rox.setup("5c528ffeaf23cf07f9bb3a85").result()
#Rox.setup("5c528ffeaf23cf07f9bb3a85")
print("Finished setup "+  str(int(round(time.time() * 1000))))

print("Time taken " + str(int(round(time.time() * 1000)) - start))


if (my_container.spankyChat.is_enabled() == True):
    print('ENABLED')
else:    
    print('NOT ENABLED')



def rollout_webhook(request):
    """HTTP Cloud Function. Using: http://flask.pocoo.org/docs/1.0/api/#flask.Request

    This will take a webhook and kill the apporopriate rollout experiment (thereby halting the rollout!)

    USAGE and parameters: 
        Query parmeters are used to pass the rollout app and secret details. 
        POST or GET to a URL once deployed as a google function or similar:
            https://DEPLOYED_FUNCTION_URL?secret=API_Token&app_id=YOUR_APP_ID&environment_name=YOUR_ENV_NAME&flag_name=YOUR_FLAGN_AME

    For example: 
        curl -X POST "https://us-central1-micprojects.cloudfunctions.net/rollout_webhook?secret=..&app_id=..&environment_name=..&flag_name=.."

    Rollout setup info: 
        See https://support.rollout.io/reference for details on how to get your app id and api token.

    Google cloud function deploying: 
        gcloud functions deploy rollout_webhook --trigger-http --runtime "python37"    

    """

    if (my_container.spankyChat.is_enabled() == True):
        return "ENABLED"
    else:    
        return 'OK'


