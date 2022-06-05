
charkheshha = input()
x = (5,2)
y = (3,4)
z = (1,6)
for i in charkheshha:
    if i == 'a':
        x,z = z,x[::-1]

    if i == 'b':
        x, z = z[::-1], x

    if i == 'c':
        x , y = y[::-1],x
    if i == 'd':
        x,y = y , x[::-1]
    if i == 'e':
        y,z = z[::-1],y
    if i == 'f':
        y,z = z,y[::-1]


print(x[0])