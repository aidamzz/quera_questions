from re import S


with open('metro.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

station = [i.split(' ') for i in lines]

n = int(input())
l = []
o = []
for i in range(n):
    mabda , maghsad = input().split(' ')
    o.append((mabda, maghsad))
for j in o:
    (mabda, maghsad) = j
    for i in range(7):
        if mabda in station[i]:
            index_mabda = i
        if maghsad in station[i]:
            index_maghsad = i

    if index_mabda == index_maghsad:
        t = station[index_mabda].index(maghsad) 
        t2 = station[index_mabda].index(mabda)
        fasele = abs(t-t2)
        l.append(29 + fasele*2)
    else:
        avaz = set(station[index_mabda]).intersection(set(station[index_maghsad]))

for i in l: 
    print(i)
