import re


def separator(ls):
    zoj = []
    ford = []
    for i in ls:
        if i%2 == 0:
            zoj.append(i)
        else:
            ford.append(i)
    return (zoj,ford)