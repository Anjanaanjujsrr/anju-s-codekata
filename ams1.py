Num=int(input())
su=0
t1=Num
while(Num>0):
    x1=Num%10
    su=su+(x1*x1*x1)
    Num=Num//10
if su==t1:
    print("yes")
else:
    print("no")