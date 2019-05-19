#anju
import re
x=input()
if re.findall("[a-zA-z2-9]",x):
    print("no")
else:
    print("yes")