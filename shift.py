reshte = input()
double_reshte = reshte+ reshte

lenght = len(reshte)
for i in range(1,lenght):
    t = double_reshte[i:lenght+i]

    if t < reshte :
        reshte = t
print(reshte)