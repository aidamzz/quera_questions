import numpy as np
n = int(input())
a = input()
b = input()

a = [i for i in a]
b = [i for i in b]
a1 = np.array(a)
b2 = np.array(b)
c = (a1 == b2)
m = [1 for i in c if i == False]

print(len(m))