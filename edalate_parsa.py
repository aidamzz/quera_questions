a, b = map(int, input().split(' '))
if b % a == 0:
    k = b//a
    l = []
    for i in range(a):
        l.append(k)
    s = " ".join([str(j) for j in l])
    for i in range(a):
        print(s)
else:
    k = b//a
    n2 = b - k*a
    n1 = a - n2
    l = []
    for i in range(n1):
        l.append(k)
    for i in range(n2):
        l.append(k+1)
    for i in range(a):
        l1 = l[i::] + l[0:i]
        print(" ".join([str(j) for j in l1]))
