n,C = input().split(' ')
l = map(int,input().split(' '))
l = list(l)
def taghsim(numbers,tedad,zarfiat):
    p = []
    numbers = sorted(numbers)
    for i in range(tedad):
        k = []
        k.append(numbers.pop())
        p.append(k)
    
    while len(numbers) != 0:
        jam = [sum(o) for o in p ]
        kamtarin = min(jam)
        araye = jam.index(kamtarin)
        p[araye].append(numbers.pop())
        if sum(p[araye] ) > zarfiat:
            return False
            break
    return True


if sum(l) <= int(C):
    print(1)
elif max(l) > int(C):
    print(0)
else:
    m = int(sum(l)/int(C))
    while taghsim(l,m,int(C)) != True:
        m +=1
    print(m)