n = int(input())

vatars = [int(input()) for i in range(n)]

def right_a(p):
    l = []
    for b in range(1, p // 2):
        a = (2*b*p - p**2) / (2 * (b - p))
        if a % 1:
            continue
        a = int(a)
        l.append(p - a - b)
    return l
        
for i in vatars:
    a = 4
    n = int(i/2)-1
    k = n** 2
    if i == 1 or i == 0:
        print(0)
    else:
        while n  < i:
            t = i**2 - k 
            if int(t**(0.5)) == t**(0.5):
                a = 1
                print(1)
                break
            n += 1 
            k = n ** 2
        if a != 1:
            print(0)
        
    