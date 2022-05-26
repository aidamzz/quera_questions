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
    for j in range(k):
        i.append(0)

for i in range(n):
    for j in range(len(l2[0])):
        for k in range(m):

            l3[i][j] += l1[i][k]*l2[k][j]

for i in l3:
    print(' '.join([str(j) for j in i]))