i=0
s = [int(i) for i in input().split()]
d = len(s)

while i<d-1:
        print(s[i+1] +s[i-1], end=' ')
        i+=1
if d!=1:
	print(s[i-i] +s[i-1])
if d == 1:
	print(s[i])