number_of_exersie = int(input())
deadline = map(int, input().split(" "))

t = number_of_exersie
l = []
for i in range(n, -1, -1):
    if max(deadline) > t:
        print()