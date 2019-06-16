l = [int(i) for i in input().split()]
a = int(input())
i=0
k=0
for i in range(len(l)): 
    if l[i] == a:
        print(i, end=' ')
        k+=1
if k==0:
    print('Отсутствует')