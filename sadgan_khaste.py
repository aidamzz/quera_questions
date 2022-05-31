a = input()
b = input()

def barax(a,b):
    if a == '':
        return 'mosavi'
    if int(a[0]) > int(b[0]):
        return True
    elif a[0]== b[0]:
        return barax(a[1:],b[1:])
    else:
        return False

if barax(a[::-1],b[::-1]) == 'mosavi':
    print('{} = {}'.format(a,b))
elif barax(a[::-1],b[::-1]):
    print('{} < {}'.format(b,a))
else:
    print('{} < {}'.format(a,b))