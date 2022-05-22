n, q = input().split(' ')
incomes = input()
incomeslist = map(int, incomes.split(' '))

allincomes = sum(incomeslist)
n = int(n)
l = []
for i in range(int(q)):
    a = int(input())
    jam = (pow(2, a-n-1, 1000000007)*allincomes % 1000000007)
    l.append(str(jam))
print('\n'.join(l))
