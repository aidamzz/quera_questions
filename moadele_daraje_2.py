a = float(input())
b = float(input())
c = float(input())

jazr = pow(b, 2) - 4*a*c

if a != 0:
    if jazr < 0 :
        print('IMPOSSIBLE')
    elif c == 0:
        answer = (-1*b)/a
        if answer>0:
            print('{:.3f}'.format(0))
            print('{:.3f}'.format(answer))
        else:
            print('{:.3f}'.format(answer))
            print('{:.3f}'.format(0))

    else:
        answer1 = ((b*(-1)-(jazr**0.5))/(2*a))
        answer2 = ((b*(-1)+(jazr**0.5))/(2*a))

        if answer1 > answer2:

            print('{:.3f}'.format(answer2))
            print('{:.3f}'.format(answer1))
        else:

            print('{:.3f}'.format(answer1))
            print('{:.3f}'.format(answer2))

else:
    if b == 0:
        print('IMPOSSIBLE')
    else:
        if c == 0:
            print('{:.3f}'.format(0))
        else:
            answer = ((-1)*c)/b
            print('{:.3f}'.format(answer))
