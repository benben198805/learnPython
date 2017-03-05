print('python can print 中文')
print('\'A\' code is',ord('A'))
print('\'中\' code is',ord('中'))


print('-------------------')

print('code 66 is',chr(65))
print('code 25991 is',chr(25991))

print('-------------------')
print('\'ABC\''' length is',len('ABC'))
print('\'中文\''' length is',len('中文'))
print('utf-8 \'中文\''' length is',len('中文'.encode('utf-8')))


print('-------------------')
print('hello %s' % 'world');
print('%s is %d height' % ('Yao Ming', 2.2));


print('---------exercise----------')
s1 = 73
s2 = 85

r = (s2-s1)/s1 * 100
print('increase %f %%' % r)




