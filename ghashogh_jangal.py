n = int(input())
s = input()
dic = {i:[] for i in range(n)}
i = 0
while i != len(s):
    for j in dic.keys():
        dic[j].append(s[i])
        i += 1
b = True
for k in dic.values():
    if 'S' not in k:
        b = False
    if 'F' not in k:
        b = False
if b:
    print('YES')
else:
    print("NO")