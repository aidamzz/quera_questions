a = '1'
i = 2
n = int(input())
while len(a)< n:
    a += str(i)
    i += 1
print(a[n-1])