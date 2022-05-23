t = int(input())
l = []
for i in range(t):
    n = int(input())
    l1 = []
    for j in range(2,n+2):
        l1.append(str(j))
        l1.append(str(2*(j)*(j+1)))
    l.append(l1)
for i in l:
    print(' '.join(i))