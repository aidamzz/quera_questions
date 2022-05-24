import math
def aval(n):
    a = 2
    while a<= math.sqrt(n):
        if n%a<1:
            return False
        a +=1
    return True
def jam(n):
    if n == 1:
        return 1
    else:
        if aval(n):
            f = pow(n,2)+1
            return f
        else:
            f = pow(n,2)+ math.gcd(n, jam(n-1))
            return f   


n = int(input())
l = []
for i in range(n):
    k = int(input())
    l.append(str(jam(k)))

print('\n'.join(l))