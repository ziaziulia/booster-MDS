s = input()
a = len(s)
i = 0
k = 1
while i<a-1:
	if s[i]==s[i+1]:
		k+=1
		i+=1
	else:
		print(s[i] + str(k), end='')
		i+=1
		k = 1
print(s[i] + str(k), end='')