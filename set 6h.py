N,K=input().split()
N=int(N)
K=int(K)
H=list(map(int,input().split()))
if(K in H):
	print("yes")
else:
	print("no")