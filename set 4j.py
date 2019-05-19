N=input()
N=int(N)
A=1
B=1
if(N==1):
    print(A,end='')
count=0
if(N>1):
    while(count<N):
        if(count==N-1):
            print(A,end='')
        else:
            print(A,end=' ')
        Nth=A+B
        A=B
        B=Nth
        count=count+1
