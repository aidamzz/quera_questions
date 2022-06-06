n, m, maxPackage, maxWeight = map(int, input().split(' '))
tozi_dic ={}
for i in range(m):
    a, b = map(int, input().split(' '))
    if a not in tozi_dic.keys():
        tozi_dic[a] = [b]
    else:
        tozi_dic[a].append(b)

def taghsim(numbers,tedad,zarfiat):
    p = []
    numbers = sorted(numbers)
    for i in range(tedad):
        k = []
        k.append(numbers.pop())
        p.append(k)
    
    while len(numbers) != 0:
        jam = [sum(o) for o in p ]
        kamtarin = min(jam)
        araye = jam.index(kamtarin)
        p[araye].append(numbers.pop())
        if sum(p[araye] ) > zarfiat:
            return False
            break
    return True

m = 0
for i in tozi_dic.keys():
    tedad = len(tozi_dic[i])
    if tedad/maxPackage != int(tedad/maxPackage):
        tedad = int(tedad/maxPackage) +1
    else:
        tedad = int(tedad/maxPackage)
    
    if tedad ==1:
        if sum(tozi_dic[i])<= maxWeight:
            m += 2
        else:
            m += tedad*2
            while taghsim(tozi_dic[i],tedad,maxWeight) != True:
                m +=2
    else:


        m += tedad*2
        while taghsim(tozi_dic[i],tedad,maxWeight) != True:
            m += 2
print(m)



