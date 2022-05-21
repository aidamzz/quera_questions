m, n = input().split(' ')
mails = input()
mails_list = mails.split(' ')
def rotate(l, n):
    return l[n:] + l[:n]
max_mails = max(mails_list, key=mails_list.count)
count_maxmails = mails_list.count(max_mails)
if count_maxmails > int(m)/2:
    print('NO')
else:
    print('YES')