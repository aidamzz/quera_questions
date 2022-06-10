n = int(input())
l = []
for i in range(n):
    l.append([int(j) for j in input().split(' ')])

lt = []

for i in range(n):
    if l[i][i] % 3 == 1:
        lt.append(l[i][i])

for i in range(n):
    if l[n-1-i][i] % 3 == 1:
        if (n-1-1) != i:
            lt.append(l[n-1-i][i])

print(sum(lt))


