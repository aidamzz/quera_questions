a = int(input())
b = int(input())
l = []
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i != 1:
            print(i)
            