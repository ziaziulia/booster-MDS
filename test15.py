s=0
c=0
d = int(input())
s+=d
c+=d*d
while s!=0:
	d = int(input())
	c+=d*d
	s+=d
print(c)