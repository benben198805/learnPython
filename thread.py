import time, threading

def loop():
    print('thread %s is running...'%threading.current_thread().name)
    n=0
    while n<10:
        n=n+1
        time.sleep(0.5)
        print('thread %s >> %s'%(threading.current_thread().name, n))
    print('thread %s ended.'%threading.current_thread().name)



print('thread %s is running...'%threading.current_thread().name)
t = threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended'%threading.current_thread().name)