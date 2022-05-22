n, q = input().split(' ')
incomes = input()
incomeslist = map(int, incomes.split(' '))

allincomes = sum(incomeslist)
n = int(n)
l = []
for i in range(int(q)):
    a = int(input())
    jam = (2**(a-n-1)*allincomes)%(10**9 +7)
    l.append(str(jam))
print('\n'.join(l))
