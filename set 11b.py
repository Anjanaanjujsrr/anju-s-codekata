import math
def div(num):
    if num%2==0:
        return div(num/2)
    else:
        return math.ceil(num)
num=int(input())    
print(div(num))    
    