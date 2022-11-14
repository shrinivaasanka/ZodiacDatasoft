##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
###############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
##############################################################################################################################################
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io
##############################################################################################################################################

from collections import defaultdict
from collections import deque
from threading import Thread
import psutil
import random
import time
import sys
import asyncio

dynamic_hashmap_dict=defaultdict(list)
process_queue=deque()
elapsedclockticks=0

def clockticks():
#async def clockticks():
    global elapsedclockticks
    while True:
        elapsedclockticks += 1 
        print("clockticks(): elapsedclockticks = ",elapsedclockticks)
        time.sleep(1)
        #await asyncio.sleep(1)

def countdown_keys():
#async def countdown_keys():
    global dynamic_hashmap_dict
    while True:
        new_dynamic_hashmap_dict=defaultdict(list)
        dynamic_hashmap_dict_keys=dynamic_hashmap_dict.keys()
        for k in list(dynamic_hashmap_dict_keys):
            new_dynamic_hashmap_dict[k-1] = dynamic_hashmap_dict.pop(k) 
        dynamic_hashmap_dict=new_dynamic_hashmap_dict
        print("countdown_keys(): dynamic_hashmap_dict = ",new_dynamic_hashmap_dict)
        time.sleep(1)

def survival_index_scheduler():
#async def survival_index_scheduler():
    global elapsedclockticks
    while True:
        time.sleep(1)
        #await asyncio.sleep(1)
        try:
            process=process_queue.popleft()
        except IndexError:
            print("IndexError")
            continue
        dynamic_hashmap_dict[process[1]].append(process[0])
        print("survival_index_scheduler():",dynamic_hashmap_dict)

def process_stream(numprocesses):
#async def process_stream():
    for n in range(numprocesses):
        process_id=random.randint(1,10000)
        deadline=random.randint(30,50)
        process_queue.append((process_id,deadline))
        print("process_stream(): process_queue = ", process_queue)
        time.sleep(1)
        #await asyncio.sleep(1)

if __name__=="__main__":
    sys.setswitchinterval(1.0)
    thread1 = Thread(target=process_stream,args=[10])
    thread2 = Thread(target=clockticks)
    thread3 = Thread(target=survival_index_scheduler)
    thread4 = Thread(target=countdown_keys)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    #asyncio.run(process_stream())
    #asyncio.run(clockticks())
    #asyncio.run(survival_index_scheduler())
