a,b=map(int,input().split())
l=[]
for i in range(a+1,b):
    s=0
    for i1 in range(2,((i//2)+1)):
        if i%i1==0:
            s=s+1
    if s==0:
        l.append(i)
k=len(l)
for digit in range(k-1):
    print(l[digit],end=' ')
print(l[k-1],end='')  
