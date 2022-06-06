l = []
for i in range(5):
    a = input()
    if a.find('FBI') != -1:
        l.append(i+1)
if l == []:
    print('HE GOT AWAY!')
else:
    for i in l:
        print(i, end=' ')