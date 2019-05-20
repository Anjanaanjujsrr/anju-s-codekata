#anju
string=str(input())
K=0
for i in range(0,len(string)):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u" or string[i]=="A" or string[i]=="E" or string[i]=="I" or string[i]=="O" or string[i]=="U":
        K=K+1
if K!=0:
    print("yes")
else: print("no")