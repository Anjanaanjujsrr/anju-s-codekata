N,K=map(int,input().split())
L=list(map(int,input().split()))
G=[]
for i in L:
	if i%2==1:
		G.append(i)
print(G[K-1])