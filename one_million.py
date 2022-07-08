n = int(input())
l = []
for i in range(n):
    n,m,a,b = map(int, input().split(' '))
    l.append([n,m,a,b])


for i in l:
    n,m,a,b = i[0], i[1], i[2], i[3]
    satr = 0
    soton = 0
    if a == 1:
        if b == 1:
            print(n*m)
        else:
            while m > b:
                m -=b-1
                m -= b
                satr += 1
            if m == b:
                satr += 1
            print(satr*n)
    else:
        if b == 1:
            while n >a:
                n -= a-1
                n -= a
                soton += 1
            if n == a:
                soton += 1
            print(soton*m)
        else:
            while m > b:
                    m -= b-1
                    m -= b
                    satr += 1
            if m == b:
                satr += 1
            while n >a:
                n -= a-1
                n -= a
                soton += 1
            if n == a:
                soton += 1
            print(soton*satr)

