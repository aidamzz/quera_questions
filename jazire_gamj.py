import numpy as np
n = int(input())
l = []
for i in range(n):
    l.append([int(j) for j in input().split(' ')])

s = sum([sum(i) for i in l])

arr = np.array(l)

ind = np.argwhere(arr == 1)

            
        


    


                



