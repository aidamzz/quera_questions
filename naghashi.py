n, m , k = map(int,input().split())
l = []
for i in range(n):
    r = []
    for j in range(m):
        r.append([])
    l.append(r)
for p in range(1,k+1):
    i, j ,u = map(int, input().split(' '))
    for o in range(u):
        for t in range(u):
            l[i+o-1][j+t-1].append(p)
result = []
for i in range(n):
    for j in range(m):
        if not l[i][j] in result and l[i][j] != []:
            result.append(l[i][j])
print(len(result))