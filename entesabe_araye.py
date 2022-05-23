t = int(input())
def entedab(araye1,araye2):
    if araye1 == araye2:
        return 'YES'
    else:
        uniqe1 = set(araye1)
        uniqe2 = set(araye2)
        eshterak = uniqe1.intersection(uniqe2)
        if eshterak == uniqe2:
            return 'YES'
        else:
            return 'NO'

l = []

for i in range(t):
    n = int(input())
    a = map(int, input().split(' '))
    b = map(int, input().split(' '))
    l.append(entedab(a,b))

print('\n'.join(l))