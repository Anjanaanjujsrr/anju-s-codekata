N,M=map(int,input().split())
A=list(map(int,input().split()))
X=0
for i in range(0,len(A)):
    if A[i]==M:
        X=X+1
print(X)