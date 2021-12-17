import threading

def calistir(threadName): 
    for i in range(10000000000000000000000000000000000000000000000000*999999999999999999999999999999999999999999999999999999999999999999999999):
        print(threadName ,"[#] ON [#]\n")

t1 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t2 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t3 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t4 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t5 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t6 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))
t7 = threading.Thread(target=calistir, args = ("[?] UwU [?]\n", ))





t1.start()
t5.start()
t2.start()
t3.start()
t4.start()
t6.start()
t7.start()


