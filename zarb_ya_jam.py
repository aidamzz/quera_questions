n = int(input())
a = map(int, input().split(' '))
a = list(a)
a = sorted(a)

def jam(l):
    t1 = l[0]*l[1]
    t2 = l[0]+l[1]
    t = max(t1, t2)
    l = l[2:]
    l.append(t)
    l = sorted(l)
    return l

while len(a) != 1:
    a = jam(a)

print(a[0])