print('read all')
with open('./temp.txt', 'r') as f:
    print(f.read());

print('------------------')
print('read one line by one line')
with open('./temp.txt', 'r') as f:
    for line in f.readlines():
        print(line)

print('------------------')
print('read by bytes')
with open('./temp.txt', 'rb') as f:
    print(f.read());

print('------------------')
print('write sth')
with open('./temp.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('123.45')


with open('./temp.txt', 'r') as f:
    print(f.read());