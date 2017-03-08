import os

print('process %s start'%os.getpid())

pid = os.fork()

if pid == 0:
    print('this is a child process %s and parent is %s'%(os.getpid(), os.getppid()))
else:
    print('praent %s create a child process %s'%(os.getpid(), pid))