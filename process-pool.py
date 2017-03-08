from multiprocessing import Pool
import os, time, random

def child_task(name):
    print('this is child task,%s(%s)'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('task %s run %0.2fs'%(name, (end-start)))

if __name__ == '__main__':
    print('this is parent process,%s'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(child_task, args=(i,))
    print('wait for child task complete')
    p.close()
    p.join()
    print('all child task done')
