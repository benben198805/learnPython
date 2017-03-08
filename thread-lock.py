import time, threading

balance = 0
lock = threading.Lock()

def change(n):
    global balance
    balance = balance + n
    balance = balance - n


def run(n):
    for i in range(100000):
        change(n)

def runThread():
    t1 = threading.Thread(target=run, args=(5,))
    t2 = threading.Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(balance, ' no lock')



def runWithLock(n):
    for i in range(100000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


def runThreadWithLock():
    t3 = threading.Thread(target=runWithLock, args=(5,))
    t4 = threading.Thread(target=runWithLock, args=(8,))
    t3.start()
    t4.start()
    t3.join()
    t4.join()

    print(balance, ' with lock')

print('run thread for 20 times:')
for i in range(20):
    runThread()

balance = 0

print('run thread with lock for 20 times:')
for i in range(20):
    runThreadWithLock()