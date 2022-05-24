
def findNumberOfTriangles(arr, n):
    a = False
    count = 0

    for i in range(n):
        for j in range(i + 1, n):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] > arr[k] and
                    arr[i] + arr[k] > arr[j] and
                    arr[k] + arr[j] > arr[i]):
                    a = True
                    break
    return a

l = map(int, input().split(' '))
l = list(l)
s = len(l)
if findNumberOfTriangles(l, s):
    print('YES')
else:
    print('NO')