n = int(input())
temp = map(int, input().split(' '))

for i in temp:
    if i> 15:
        print("cooler")
    else:
        print("heater")