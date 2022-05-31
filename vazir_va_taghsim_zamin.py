n = input()
l = map(int, input().split(' '))
l = list(l)

def taghsim(l,m):
    k = []
    o = []
    l = sorted(l)

    for i in range(m):
        o = []
        a = l.pop()
        o.append(a)
        k.append(o)
    for i in l:
        m = [sum(j) for j in k]

        kamtarin = min(m)
        index_kamtarin = m.index(kamtarin)
        k[index_kamtarin].append(i)
    return k
p = l   
        
m = max(l)
if len(l) < 3:
    p = [1]
else:
    while len(set(p)) != 1:
        l1 = l
        if sum(l1)/m == sum(l1)//m:
            p = taghsim(l1,sum(l1)//m)
            p1 = [sum(j) for j in p]
            p2 = [len(j) for j in p]
            if len(set(p1)) == 1:
                p = p2
            else:
                p = p1

        m +=1
print(len(p))

