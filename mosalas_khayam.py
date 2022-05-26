n = int(input())


def satr(n):
    ll= []
    if n == 3:
        l = [1,1]
        ll.append(l[0])
        a = sum(l)
        ll.append(a)
        ll.append(l[1])
        return ll
    else:
        l = satr(n-1)

        b = len(l)-1
        ll.append(l[0])
        for i in range(0,b):
            if i != b:

                a = l[i]+ l[i+1]
                ll.append(a)
        ll.append(l[-1])
        return ll
if n >= 1:
    print(1)
if n>=2:
    print(1,1)
if n>=3:
    for j in range(3,n+1):
        print(' '.join([str(i)  for i in satr(j)]))
