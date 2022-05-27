n = int(input())
budje = {}
hedye = {}
for i in range(n):
    k = input()
    budje[k]= 0
    hedye[k]= 0
for i in range(n):
    k = input()
    m , l = map(int, input().split(' '))
    if l != 0:
        if m%l != 0:
            a = m - m%l
            budje[k] -= a
            a = int(a/l)
            for i in range(l):
                name = input()
                hedye[name] += a
        else:
            budje[k] -= m
            for i in range(l):
                name = input()
                a = int(m/l)
                hedye[name] += a

for i in budje.keys():
    print(i, budje[i]+hedye[i])