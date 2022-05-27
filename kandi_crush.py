n = int(input())
l = []
for i in range(n):
    a = input().split()
    l.append(a)

m = []
for i in range(n):

    for j in range(i,-1,-1):

        for k in range(0,i+1):
            print(i,j, k)
            if j ==k :
                if k >= i:
                    if j-k >= 0:
                        o = l[j-k][k]
                        print(o)
                        m.append(o)
            else:
                if j-k >= 0:
                        o = l[j-k][k]
                        print(o)
                        m.append(o)
