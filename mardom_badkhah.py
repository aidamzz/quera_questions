n, m = map(int,input().split(' '))
if n> m:
    n = m 
if m> n:
    m = n

if m%2 ==0:
    print('white')
else:
    print('black')




