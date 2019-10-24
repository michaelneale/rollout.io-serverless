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
# Feature flags state is managed as an object instance and updated live by Rollout
# Treat it as read only in your function. 
#
class MyContainer:
     def __init__(self):
        self.enable_tutorial = RoxFlag()
my_container = MyContainer()
Rox.register('', my_container)


# 
# Here we load the state of the flags as a one off for a cold start. 
# If this is too slow you can skip the .result() call and it will use defaults while
# the flags are loaded in the background. 
#
start = current_time()
Rox.setup("..environment key here..").result()
stopwatch(start, "Setup time")


#
# This will show the state of the flag at the time of a cold start.
#
if (my_container.enable_tutorial.is_enabled() == True):
    print('ENABLED')
else:    
    print('NOT ENABLED')


#
# Finally, your function that does the thing!
# Everything until this point is called once during a "cold start" of the function. 
# This function can be re-used when warm. Rollout will keep the flags up to date. 
#
def my_function(request):
    """HTTP Cloud Function. Using: http://flask.pocoo.org/docs/1.0/api/#flask.Request

    Rollout setup info: 
        QuickStart: https://support.rollout.io/docs/initial-setup
        You will need the Install Instructions from in app to get the ID used above in Rox.setup (and your flag name of course)

    Google cloud function deploying: 
        gcloud functions deploy my_function --trigger-http --runtime "python37"    

    """

    if (my_container.enable_tutorial.is_enabled() == True):
        return 'ENABLED'
    else:    
        return 'NOT ENABLED'


