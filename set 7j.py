#anju
N=int(input())
for i in range(0,1000):
    if 2**i==N:
        break
i=i+1
print(2**i)