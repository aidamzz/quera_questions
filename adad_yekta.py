n = input()
list_adad = input().split(' ')
list_yekta = [int(i) for i in list_adad if list_adad.count(i) == 1]
if list_yekta == []:
    print(0)
else:
    first = list_yekta.pop()

    while list_yekta != []:
        first = first ^ list_yekta.pop()

    print(first)
