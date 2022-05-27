n = int(input())

lister = []
for i in range(n):
    lister.append(input())

print(max([len(set(i)) for i in lister]))
