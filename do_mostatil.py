n = int(input())
unique_or_not = []
oo =[]

for n1 in range(n):
    o = []
    max_x = 0
    max_y = 0
    y_index1 = []
    y_index2 = []
    x_index1 = []
    x_index2 = []
    n2,m2 = input().split(' ')
    n2 = int(n2)
    mat = []
    b = ''
    satrx = 0
    satry = 0
    for i in range(n2):
        a = input()
        b += a
        a = [j for j in a]
        if '+' in a:
            satrx +=1
            tedad = a.count('+')
            if tedad > max_x:
                x_index1.append([i+1,a.index('+')+1])
                max_x = tedad
            elif '-' in a:
                if a.index('-')> a.index('+'):

                    x_index2.append([i+1,a.index('-')])
                    y_index2.append([i+1,a.index('+')+1])
                else:
                    x_index2.append([i+1,a.index('+')])
                    y_index2.append([i+1,a.index('-')+1])
                
                
        if '-' in a:
            satry += 1
            tedad = a.count('-')
            if tedad > max_y:
                y_index1.append([i+1,a.index('-')+1])
                max_y = tedad

    if '+' in b:
        if '-' in b:
            unique_or_not.append('unique')
        else:
            unique_or_not.append('not unique')          
    else:
        unique_or_not.append('not unique')
    if x_index2 == []:
        u = [x_index1[-1][0]+satrx-1,x_index1[-1][1]+max_x-1]
        x_index2.append(u)
    if y_index2 == []:
        u = [y_index1[-1][0]+satry-1,y_index1[-1][1]+max_y-1]
        y_index2.append(u)
    p = []
    for i in x_index1[-1]:
        p.append(i)
    for j in x_index2[-1]:
        p.append(j)
    o.append(p)
    p = []
    for i in y_index1[-1]:
        p.append(i)
    for j in y_index2[-1]:
        p.append(j)
    o.append(p)
    oo.append(o)