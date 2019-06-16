d = int(input())
n = 1
f = 0
c = []
while n!=100:
	f = [str(n)]*n
	a = [n]*n
	c += f
	n += 1
print(*c[:d])