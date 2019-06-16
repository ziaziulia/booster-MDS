i=0
s = [int(i) for i in input().split()]
a=s
d = len(a)
nonunique_list = sorted(set([i for i in s if s.count(i)>1]))
d = len(nonunique_list)
while i<d:
	print(nonunique_list[i], end=' ')
	i+=1