a = int(input())
b = int(input())
c = int(input())
def mabna10(a,n):
    if a == 0:
        return 0
    else:
        a = str(a)
        j = int(a[0])
        s = j*n
        for i in a[1:len(a)-1]:
            i = int(i)
            s += i
            s = s*n
        s += int(a[-1])
        return s
def mabna(a, b):
    if a == 0:
        return 0
    else:
        l = []
        while a:
            l.append(int(a%b))
            a //= b
        return int(''.join(str(i) for i in l[::-1]))
 
adad_mabna10 = mabna10(a,b)
adad_mabnac = mabna(adad_mabna10, c)
if len(str(adad_mabnac)) %2 != 0:
    z = str(adad_mabnac)
    z1 = z[:int(len(z)/2)]
    z2 = z[(int(len(z)/2)+1):]
    if z1 == z2[::-1]:
        print('YES')
    else:
        print('NO')
else:
    z = str(adad_mabnac)
    z1 = z[:int(len(z)/2)]
    z2 = z[int(len(z)/2):]
    if z1 == z2[::-1]:
        print('YES')
    else:
        print('NO')
