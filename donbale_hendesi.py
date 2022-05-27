import numpy
n, m = input().split(' ')
l = []
for i in range(int(n)):
    k = map(int, input().split(' '))
    k = list(k)
    l.append(k)

def geo(a, r, length):
    geometric = [a * r ** (n - 1) for n in range(1, length + 1)]
    return geometric

m = []
for i in l:

    if len(set(i)) == 1:
        m.append(len(i))
    else:
        m1 = []
        for j in range(len(i)):
            if j == len(i)-1:
                r = i[j]/i[j-1]
                length = 1
                m1.append(1)
            else:
                r = i[j+1]/i[j]
                length = len(i[j:])
            
                t = geo(i[j], r, length)
                t1 = numpy.array(t)
                t2 = numpy.array(i[j:])
                t3 = (t1 == t2)

                x = 0
                for i1 in t3:
                    if i1 == True:
                        x += 1
                    else:
                        break
                m1.append(x)
        pp = max(m1)
        m.append(pp)
print(min(m)*int(n))
