a = input()
if a.count('G') == 0:
    print('nakhor lite')
else:
    if a.count('R') >2:
        print('nakhor lite')
    else:
        if a.count('R')>1:
            if a.count('Y')>1:
                print('nakhor lite')
            else:
                print('rahat baash')
        else:
            print('rahat baash')