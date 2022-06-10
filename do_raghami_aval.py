
l = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
a = input()
l2 = {}

for i in l:
    if i in a:
        if a.count(i) >1:
            k = list_duplicates_of(a,i)
            for j in k:
                l2[j]= i
        else:
            l2[a.index(i)]= i



sorte_k = sorted(l2.keys())

for i in sorte_k:
    print(l2[i])