#anju
K=int(input())
N=list(map(int,input().split()))
X=sorted(N)
for i in range(0,len(N)):
    if X[i]!=N[i]:
        print(i)
        break