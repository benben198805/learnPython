import re

re_email = re.compile(r'^[\w.]*@\w*\.com$')

result1 = re_email.match('someone@gmail.com')
print(result1)

result2 = re_email.match('bill.gates@microsoft.com')
print(result2)