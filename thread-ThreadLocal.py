import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, I am a %s %s and am %s years old.(from %s)'%(std['sex'], std['name'], std['age'], threading.current_thread().name))


def process_thread(name, other):
    local_school.student = {
        'name':name,
        'sex':other['sex'],
        'age':other['age']
    }
    process_student()


t1 = threading.Thread(target=process_thread, args=('Boo',{'age':12,'sex':'male'}),name = 'Thread-A')
t2 = threading.Thread(target=process_thread, args=('Poo',{'age':14,'sex':'female'}),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()