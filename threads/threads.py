import threading
import time


def t_sum(a,b):
    time.sleep(5)
    print(a+b)
    return (a+b)

def t_res(a,b):
    time.sleep(6)
    print(a-b)
    return (a-b)

def t_prod(a,b):
    time.sleep(7)
    print(a*b)
    return (a*b)

def t_div(a,b):
    print(a/b)
    return (a/b)

v1=10
v2=5

threads=[]

t1 = threading.Thread(target=t_sum, args=(v1,v2))
t2 = threading.Thread(target=t_res, args=(v1,v2))
t3 = threading.Thread(target=t_prod, args=(v1,v2))
t4 = threading.Thread(target=t_div, args=(v1,v2))

threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

t1.start()
t2.start()
t3.start()
t4.start()
