#anju
num=int(input())
sum=0
for i in range(2,num):
    if num%i==0:
        sum=1
if sum==0:
    print("no")
else: print("yes")