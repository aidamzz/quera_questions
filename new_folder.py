n = int(input())
folders = [input() for i in range(n)]
dic_folders = {}
list_folders = []
for i in folders:
    if i in dic_folders.keys():
        a = "'{} ({})'".format(i,str(dic_folders[i]))
        list_folders.append(a)
        dic_folders[i] +=1
    else:
        if i in folders:
            a = "'{} ({})'".format(i,str(1))
            list_folders.append(a)
            dic_folders[a] =1
        else:
            dic_folders[i] = 1
            a = "'{} '".format(i)
            list_folders.append(a)
    print(list_folders)
    list_folders = sorted(list_folders)
    print(', '.join(k for k in list_folders))