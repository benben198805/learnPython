from multiprocessing import Process
import os

def runChildProcess(name):
    print('this is child process,%s(%s)'%(name, os.getpid()))

if __name__ == '__main__':
    print('this is parent process,%s'%os.getpid())
    p = Process(target=runChildProcess, args=('tom',))
    print('child start')
    p.start()
    p.join()
    print('child end')
