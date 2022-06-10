def next_number(s):
    result = []
    i = 0
    while i < len(s):
        counter = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1 
            counter += 1

        result.append(str(counter)+s[i])
        i +=1
    return ''.join(result)

a = input()
print(next_number(a))