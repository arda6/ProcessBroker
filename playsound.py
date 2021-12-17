import threading
import os
def calistir(threadName): 
    for i in range(7):
        os.system("python playsound2.py")
        print(threadName ,"[ # ] Process Complated [ # ]\n")

t1 = threading.Thread(target=calistir, args = ("[ 1 ] Process Started [ 1 ]\n", ))
t2 = threading.Thread(target=calistir, args = ("[ 2 ] Process Started [ 2 ]\n", ))

t1.start()
t2.start()
