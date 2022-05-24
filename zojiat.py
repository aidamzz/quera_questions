import math
def aval(n):
    a = 2
    while a<= math.sqrt(n):
        if n%a<1:
            return False
        a +=1
    return True
n = int(input())
if n == 1:
    print('fard')
else:
    if n % 2 != 0:
        if aval(n):
            print('zoj')
        else:
            print('fard')
    else:
        print('fard')