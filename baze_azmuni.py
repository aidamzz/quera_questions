s, f,l ,x = map(int,input().split(' '))
if x< s:
    print('exam did not started!')
else:
    if x>= f:
        print('exam finished!')
    else:
        y = f-x
        if y >l:
            print(l)
        else:
            print(y)