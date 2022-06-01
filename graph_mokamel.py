n, m = input().split(' ')
l = {}

for i in range(int(m)):
    k, j = input().split(' ')
    if k in l.keys():
        l[k].append({k,j})
        if j in l.keys():
            l[j].append({k,j})
        else:
            l[j] = [{k,j}]
    else:
        l[k] = [{k,j}]
        if j in l.keys():
            l[j].append({k,j})
        else:
            l[j] = [{k,j}]

m1 = int(input())
p = []

for i in range(m1):
    k, j = input().split(' ')
    if k in l.keys() and ({k,j} in l[k]):
        p.append('NO')
    else:
        p.append('YES')


for i in p:
    print(i)



