n = int(input())
l = []
for i in range(n):
    a,b = map(int, input().split(' '))
    for j in range(a,b+1):
        l.append(j)
l = list(set(l))
x = int(input())
y = int(input())

def check(ll,target,high,low):
    if low > high:
        return False
    else:
        mid = (high+low)//2
        if ll[mid] == target:
            return True

        elif ll[mid]> target:
            return check(ll,target,mid-1,low)
        else:
            return check(ll,target,high,mid+1)
b = True

for i in range(x,y+1):
    if  not check(sorted(l),i,len(l)-1,0):
        b = False

if b:
    print('true')
else:
    print('false')
