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
        for i in range(n,-1,-1):
            if aval(i):
                f = pow(i,2)+1
                if i != n:
                    for j in range(i+1,n+1):
                        f = pow(j,2)+ math.gcd(j, f)
                return f   
                break


n = int(input())
l = []
for i in range(n):
    k = int(input())
    l.append(str(jam(k)))

print('\n'.join(l))