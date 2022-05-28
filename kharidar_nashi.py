n, m, k = [int(i) for i in input().split()]

lister = []
for i in range(k):
    lister.append([int(i) for i in input().split()])

if k % 2 != 0:
    print(0)
elif k == m * n:
    print(-1)
else:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i, j] not in lister:
                print(1, " ".join([str(i), str(j)]), sep="\n")
                break
        else:
            continue
        break
