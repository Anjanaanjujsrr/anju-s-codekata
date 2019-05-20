#anju
a=int(input())
b=list(map(int,input().split()))
sum=0
for i in range(0,a):
    sum=sum+b[i]
print(sum)