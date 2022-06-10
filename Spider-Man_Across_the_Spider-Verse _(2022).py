a,b = map(int, input().split(' '))
l = []
for i in range(a):
    p = input()
    l.append(p)

daraje = int(input())


def tabe45(l,a,b):
    l1 = []
    if daraje == 45:
        for i in range(a):
            j = i
            k = 0
            s = ' '*(a-(i+1))
            while j != -1:
                s += l[j][k]
                s += ' '
                k += 1
                j -= 1
            l1.append(s)
        for i in range(a):
            j = a-1
            k = 1+i
            s = ' '*(i+1)

            while k != b :
                s += l[j][k]
                s += ' '
                k += 1
                j -= 1

            l1.append(s)
    return l1

def tabe180(l):
    return l[::-1]

def tabe90(l, a,b):
    l1 = []
    for j in range(a):
        s = ''
        for i in range(b):
            s += l[i][j]
        l1.append(s)
    return l1







