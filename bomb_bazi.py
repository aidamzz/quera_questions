
import numpy as np
n, m = map(int,input().split(' '))
zero = np.zeros((n,m))
k = int(input())

def bomb(i,j,m):
    if i == 1:
        if j == 1:
            m[i][j-1] += 1
            m[i-1][j] += 1
            m[i][j] += 1
        elif j == len(m[0]):
            m[i-1][j-2] += 1
            m[i][j-1] += 1
            m[i][j-2] += 1
        else:
            m[i][j-1] += 1
            m[i-1][j] += 1
            m[i-1][j-2] += 1
            m[i][j-2] +=1
            m[i][j] +=1
    elif i == len(m):
        if j == 1:
            m[i-1][j] += 1
            m[i-2][j-1] += 1
            m[i-2][j]
        elif j == len(m[0]):
            m[i-1][j-2]+= 1
            m[i-2][j-2] += 1
            m[i-2][j-1] += 1
        else:
            m[i-1][j] += 1
            m[i-2][j-1] += 1
            m[i-1][j-2] +=1
            m[i-2][j-2] += 1
            m[i-2][j] += 1
    
    else:
        if j == 1:
            m[i-2][j-1] += 1
            m[i-2][j] += 1
            m[i-1][j] +=1
            m[i][j-1] +=1
            m[i][j] +=1
        elif j == len(m[0]):
            m[i-2][j-1] +=1
            m[i-2][j-2] +=1
            m[i-1][j-2] +=1
            m[i][j-1] +=1
            m[i][j-2] +=1
        else:
            m[i-1][j] += 1
            m[i-1][j-2] +=1
            m[i][j-1] += 1
            m[i-2][j-1] += 1
            m[i][j] += 1
            m[i][j-2] += 1
            m[i-2][j-2] +=1
            m[i-2][j] += 1
    return(m)
for i in range(k):
    i,j = map(int,input().split(' '))

    zero[i-1][j-1] = 9
    zero = bomb(i,j,zero)

z = zero.tolist()


for i in z:
    i = [str(int(x)) if x < 9 else '*' for x in i]
    for j in i:
        print(j, end= ' ')
    print()