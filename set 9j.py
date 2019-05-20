#anju
import re
string=input()
a=re.findall('[0-9]',string)
for  i in a:
    print(i,end='')