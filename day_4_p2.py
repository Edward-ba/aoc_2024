import re

if __name__ == '__main__':
    f = open('4.in', 'r').readlines()
    f = [i[:-1] for i in f]
    tot = 0
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == 'A':
                found = False
                if i == 0 or i == len(f) - 1 or j == 0 or j == len(f[0]) - 1:
                    continue
                for rr in [-1, 1]:
                    for cc in [-1, 1]:
                        if f[i + rr][j + cc] == 'M' and f[i - rr][j - cc] == 'S':
                            if (f[i - rr][j + cc] == 'M' and f[i + rr][j - cc] == 'S') or (
                                    f[i + rr][j - cc] == 'M' and f[i - rr][j + cc] == 'S'):
                                tot += 1
                                found = True
                                break
                    if found:
                        break

    print(tot)
