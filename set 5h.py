N=int(input())
lis=list(map(int,input().split()))
sum=0
for i in range(0,len(lis)):
   sum=sum+lis[i]
avg=sum//len(lis)
print(lis[avg-1])
