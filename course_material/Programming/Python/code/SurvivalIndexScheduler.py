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
import subprocess
import os
import json

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
        kernelanalyticsf=open("/etc/virgo_kernel_analytics.conf","a")
        time.sleep(1)
        #await asyncio.sleep(1)
        try:
            process=process_queue.popleft()
        except IndexError:
            print("IndexError")
            continue
        dynamic_hashmap_dict[process[1]].append(process[0])
        print("survival_index_scheduler():",dynamic_hashmap_dict)
        for k,v in dynamic_hashmap_dict.items():
            kernelanalyticsf.write(str(k) + " ---- " + str(v) + "\n")
        kernelanalyticsf.write(" --------------------------------------------- ")
        kernelanalyticsf.write("\n")
        kernelanalyticsf.close()

def process_stream():
#async def process_stream():
    processes=subprocess.run(["ps","-eafo","pid,cls"],capture_output=True)
    pidsched=processes.stdout.decode("utf-8").strip().split("\n")
    for p in pidsched[1:]:
        ptoks=p.split()
        process_id=ptoks[0]
        sched_policy=ptoks[1]
        if sched_policy=="DLN":
            schedparams=subprocess.run(["chrt","-p",process_id],capture_output=True)
            print(schedparams)
            schedparamstoks=schedparams.stdout.decode("utf-8").strip().split("\n")
            deadlinestring=schedparamstoks[2].split(":")
            deadlinestringtoks=deadlinestring[1].split("/")
            print("deadlinestringtoks:",deadlinestringtoks)
            deadline=deadlinestringtoks[1]
            process_queue.append((process_id,int(deadline)))
        print("process_stream(): process_queue = ", process_queue)
        time.sleep(1)
        #await asyncio.sleep(1)

def spawn_processes(no_of_processes):
    #SCHED_DEADLINE chrt example (runtime < deadline < period):
    #----------------------------------------------------------
    #chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 -p 0 <pid>
    #chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 0 <processname>
    for n in range(no_of_processes):
        os.system("chrt -d --sched-runtime 1000000 --sched-deadline 5000000 --sched-period 5000000 0 python3.11 SurvivalIndexScheduler_process.py&")

if __name__=="__main__":
    sys.setswitchinterval(1.0)
    spawn_processes(20)
    thread1 = Thread(target=process_stream)
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
