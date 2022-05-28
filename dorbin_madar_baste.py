a = input().split()
b = input().split()
c = input().split()

d1 = [a[0], b[0], c[0]]
d1 = [i for i in set(d1) if d1.count(i) == 1]
d2 = [a[1], b[1], c[1]]
d2 = [i for i in set(d2) if d2.count(i) == 1]

print(d1[0], d2[0])