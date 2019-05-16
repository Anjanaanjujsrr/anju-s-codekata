l,u=input().split()
l=int(l)
u=int(u)
for n in range(l, u):
    order = len(str(n))
    s = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //= 10
    if n == s:
       print(n,end=" ")
