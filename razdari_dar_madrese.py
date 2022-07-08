n = int(input())
con = []
for i in range(n):
    n, m, s, t = input().split(' ')
    m = int(m)
    o = []
    l = (s,t)
    o.append(l)
    for j in range(m):
        a, b = input().split(' ')
        if (a,b) not in o:
            o.append((a,b))
    con.append(o)

for l in con:
    lent = 0
    dana = []
    target = l[0][0]
    dana.append(l[0][1])
    l.pop(0)
    for i in l:
        if i[0] in dana:
            dana.append(i[1])
    if target not in dana:
        print(-1)
    else:
        print(len(dana)-1)


