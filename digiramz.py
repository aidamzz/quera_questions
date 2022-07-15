n, m = map(int, input().split(' '))
sood = []
sooda = []
for i in range(n):
    p, c = map(int, input().split(' '))
    sooda.append((p,c))

min_rooz = 1

def sud(a, k):
    sudd = 0
    for i in a:
        (p , c) = i 
        s = k*p - c
        if s>0:
            sudd += s
    return sudd

while sud(sooda, min_rooz) < m:
    min_rooz += 1

print(min_rooz)

    

