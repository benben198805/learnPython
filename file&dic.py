import os

def listFolders():
    for file in os.listdir():
        if os.path.isdir(file):
            print(file)

print('current path:',os.path.abspath('.'))

print('--------all folders--------')
listFolders()

print('--------create one folder--------')
os.mkdir('./testdir')
listFolders()

print('---------rename folder-------')
os.rename('./testdir','./123')
listFolders()


print('--------------------------')
filePath = os.path.join(os.path.abspath('.'), 'for.py')

print(os.path.split(filePath))
print(os.path.splitext(filePath))


print('------exercise------------')
def findFile(target):
    if isinstance(target, str):
        for root, dirs, files in os.walk(os.path.abspath('.')):
            for file in files:
                if file.find(target) > -1:
                    print(file)  

findFile('fo')