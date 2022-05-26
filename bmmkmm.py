import math
a , b = map(int, input().split(' '))

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(math.gcd(a,b), lcm(a, b))