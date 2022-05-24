n = int(input())
l = map(int, input().split(' '))
l = list(l)

max_l = max(l)
m = 0
a = l[0]
for i in range(len(l)):
    if l[i] == max_l:
        m += 1

        break
    else:
        if i == len(l):
            if l[i] > a:

                m += 1
        else:
            if a < l[i+1]:
                a = l[i+1]

                m += 1
print(m)