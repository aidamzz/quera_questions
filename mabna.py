def mabna(a, b):
    if a == 0:
        return [0]
    else:
        l = []
        while a:
            l.append(int(a%b))
            a //= b
        return l[::-1]
a, b = map(int, input().split())
c = mabna(a, b)
sum1 = 0
sum2 = 0
for i in range(len(c)):
    if i%2 == 0:
        sum1 += c[i]
    else:
        sum2 += c[i]
if sum1 == sum2:
    print('Yes')
else:
    print('No')
        
    