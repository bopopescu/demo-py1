#process - program in execution, not lightweight,process don't share data, more time to terminate
#thread - a segment of process, light weight processes,threads share resources, lesser time to terminate

import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self,id, name,counter):
        threading.Thread.__init__(self)
        self.threadId = id
        self.name = name
        self.counter = counter

    def run(self):
        print("starting my thread ", self.name)
        print(" counter",self.counter)
        incr_counter(self.name, 5, self.counter)
        print("ending my thread ", self.name)

def incr_counter(name,delay,counter):
    while counter:
        if exitFlag:
            name.exit()
        time.sleep(delay)
        print(" from incr ", name, time.ctime(time.time()))
        counter -= 1

t1 = MyThread(11,'thread-1',1)
t2 = MyThread(12,'thread-2',2)

t1.start()
t2.start()