#anju
N,M=map(int,input().split())
m=0
a=N*M
X=max(N,M)
for i in range(1,X+1):
    if N%i==0 and M%i==0:
        m=i
print(int(a/m))