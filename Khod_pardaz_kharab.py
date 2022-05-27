n = input()
dic = {}
for i in range(10):
    dic[i] = int(input())

a = ''
m = 0
i = 0
while a != n:
    j = int(n[i])
    m += 1

    if dic[j] == j:
        a += n[i]
        i += 1
    else:
        if len(str(dic[j]))> 1:
            m1 = 0
            for k in range(len(str(dic[j]))):
                if ((i+k) > len(n)-1):
                    h = len(n)-1
                else:
                    h = i +k
                if (str(dic[j]))[k] == n[h]:
                    m1+=1
            if m1 == len(str(dic[j])):
                a += (str(dic[j]))
                i += m1
            else:
                a += (str(dic[j]))[:m1]
                i += m1
                p = len(str(dic[j]) )- m1
                m += p
print(m)
