n, k = map(int, input().split(' '))

a = map(int,input().split(' '))
a = list(a)
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

tedad = sum(a)//k

if taghsim(a,tedad,k):
    print(n-tedad)
else:
    print(n-tedad-1)
