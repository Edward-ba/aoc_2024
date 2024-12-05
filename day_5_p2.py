import re
from operator import index

from utils import *

if __name__ == '__main__':
    f = open('5.in', 'r').readlines()
    a1 = [int(i.split('|')[0]) for i in f[:f.index('\n')]]
    a2 = [int(i.split('|')[1][:-1]) for i in f[:f.index('\n')]]
    b = [[int(j) for j in i[:-1].split(',')] for i in f[f.index('\n') + 1:]]
    # a_1 = {j:i for i, j in a.items()} # reverse
    print(a1, a2)
    print(b)
    total = 0
    for i in b:
        works = True
        r = []
        for j in range(len(i)):
            indexes = [k for k, x in enumerate(a1) if x == i[j]]
            for k in indexes:
                if a2[k] in i:
                    if a2[k] not in i[j:]:
                        works = False
                        r += k
                        break

        if works:
            continue

        total += i[len(i)//2]

    print(total)