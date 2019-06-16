test = input()
a = len(test)
b = test.lower().count('g')
c = test.lower().count('c')
s = (b+c)/a*100
print(s)