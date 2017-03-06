import pickle
import json

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
print(json.dumps(d))

with open('./temp/dump_1.txt', 'wb') as f1:
    pickle.dump(d,f1)

with open('./temp/dump_1.txt', 'rb') as f2:
    pickle.load(f2)

print('----------------------------------')

with open('./temp/dump_2.txt', 'w') as f3:
    json.dump(json.dumps(d),f3)

with open('./temp/dump_2.txt', 'r') as f4:
    text = f4.read()
    print(json.loads(text))



print('----------------------------------')

class Student(object):
    """docstring for Student"""
    def __init__(self, name,age):
        self.name = name
        self.age = age

student = Student('abc',13)

with open('./temp/dump_3.txt', 'w') as f4:
    json.dump(json.dumps(student, default=lambda obj: obj.__dict__),f4)

def dict2student(d):
    return Student(d['name'], d['age'])

with open('./temp/dump_2.txt', 'r') as f4:
    text = f4.read()
    print(json.loads(text, object_hook=dict2student))
