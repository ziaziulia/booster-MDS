a = int(input())
while a <= 100:
    if (a < 10):
        a = int(input())
        continue # переходим к следующей итерации
    else:
        print(a)
        a = int(input())