s1 = 1
n = int(input())
if n == 1:
    print(1)
else:
    for i in range(2,n+1):
        if i > 9:
            j = sum([int(k) for k in str(i)])
        else:
            j = i
        s1 = 2*s1 + j
    print(s1%(10**9 + 7))