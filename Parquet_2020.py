m, n = map(int, input().split(' '))
jam = m+n
a = 1
i = 3
while a != n:
    i +=1
    if int(jam/i) == jam//i:
        a = (i-2)*((jam//i)-2)
        
    else:
        i += 1

print(max(i,jam//i),min(i,jam//i))