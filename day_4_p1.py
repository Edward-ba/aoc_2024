import re

if __name__ == '__main__':
    f = open('4.in', 'r').readlines()
    f = [i[:-1] for i in f]
    tot = 0
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == 'X':
                for rr in [-1, 0, 1]:
                    if rr * 3 + i < 0 or rr * 3 + i < 0 >= len(f):
                        continue
                    for cc in [-1, 0, 1]:
                        if cc*3 + j < 0 or cc*3 + j >= len(f[0]):
                            continue
                        try:
                            if f[rr + i][cc + j] == 'M' and f[rr*2 + i][cc*2 + j] == 'A' and f[rr*3 + i][cc*3 + j] == 'S':
                                tot += 1
                        except IndexError:
                            continue
    print(tot)
