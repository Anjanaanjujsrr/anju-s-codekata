x,y=map(int,input().split())
z=x*y
s=z**0.5
if s**2 == z:
	print("yes")
else:
	print("no")