num,k1 = input().split() 
num = int(num)
k1 = int(k1)
for j in range(num,(k1-1),1):
    num = num+1
    if(num%2 != 0):
        print(num , end = ' ')