#anju
x=input()
z=list(x)
y=len(z)
f=0
if y%2==0:
	i=y//2
	z[i]='*'
	z[i-1]='*'
	t=''.join(z)
	print(t)
else:
	f=y//2
	c[f]='*'
	e=''.join(z)
	print(e)