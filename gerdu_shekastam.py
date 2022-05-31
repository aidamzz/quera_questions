l, w, h = map(int, input().split())
k = 0

for i in range(0, l // h + 1):
    if (l - i * h) % w == 0:
        print((l - i * h) // w, i)
        k = 1

if k == 0:
    print(-1)