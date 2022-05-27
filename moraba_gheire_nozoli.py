a = int(input())


l = map(int, input().split(' '))

l = l.sort()
print(' '.join([str(pow(i,2)) for i in l][::-1]))