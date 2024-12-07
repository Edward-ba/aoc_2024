from utils import *
import re

if __name__ == '__main__':
    f = open('7.in', 'r').read()[:-1].split('\n')
    a = {int(i.split(':')[0]): [int(j) for j in i.split(': ')[1].split(' ')] for i in f}
    print(a)
    t = 0
    for i, j in a.items():
        z = [j[0]]
        # print(j[0])
        for k in j[1:]:
            # print(k)
            z = [n*k for n in z] + [n+k for n in z]
            if i in z:
                print(i)
                print(z)
                t += i
                break

    print(t)