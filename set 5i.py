X=int(input())
K=X
S=0
while X>1:
    if X%2==0:
        X=X/2
        S=S+1
    else:
        print("no")
        break
if (2**S)==K:
    print("yes")
