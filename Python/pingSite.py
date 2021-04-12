import sys

import threading
import time
import requests

#Routine for call site periodically 
def CallSite():
    while 1:
        print (sys.argv[1])
        if sys.argv[1].startswith('http'):
            r = requests.get(sys.argv[1])
            print(f'Call For : {sys.argv[1]} Result : {r.status_code} ')
        else:
            print('Request Schema not valid...')

        time.sleep(60)

CallSite()
t1 = threading.Thread(target=CallSite)
#Background thread will finish with the main program
t1.setDaemon(True)
#Start CallSite() in a separate thread as Background worker
t1.start()


if __name__ == "__main__":
    CallSite()