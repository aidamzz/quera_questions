import numpy as np

n,m = map(int,input().split(' '))

sefr = np.zeros((n,n))

for k in range(m):
    i,j = map(int,input().split(' '))
    sefr[i-1][j-1] += 1
    sefr[j-1][i-1] += 1

for i in sefr:
    for j in i:
        print(int(j),end='')
    print()