A=input()
N=0
M=0
for C in A:
    if(C.isalpha()):
        N+=1
    elif(C.isnumeric()):
        M+=1    
if(M>0 and N>0):
    print("Yes")
else:
    print("No")