n, m , k = map(int, input().split(' '))
l1 = []
for i in range(n):
    l = map(int, input().split(' '))
    l1.append(list(l))
l2 = []
for i in range(m):
    l = map(int, input().split(' '))
    l2.append(list(l))

l3 = []
for i in range(n):
    l3.append([])

for i in l3:
    for i in range(k):
        i.append(0)
