from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
f.write('.')

print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
print(f1.read())



from io import BytesIO
f_bytes = BytesIO()
f_bytes.write('你好'.encode('utf-8'))
f_bytes.write('，'.encode('utf-8'))
f_bytes.write('世界'.encode('utf-8'))
f_bytes.write('。'.encode('utf-8'))

print(f_bytes.getvalue())