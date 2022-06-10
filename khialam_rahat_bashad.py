n = int(input())
dic_l = {}
for i in range(n):
    a,b,c = map(int,input().split(' '))
    dic_l[a] = [b,c]

a,b = map(int,input().split(' '))
i = 0
p = []
l = list(dic_l.values())

while i+1 != len(l)-1:
    o = l[i+1][0]-l[i][1]
    p.append(o)
    i +=1


for i in range(n):
    if p[i] > b:
        u = i
        break

print(l[u][1]+1,l[u][1]+1+b)