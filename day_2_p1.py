import re

if __name__ == '__main__':
    f = open('input2.txt', 'r').read().split('\n')
    a = [[int(j) for j in i.split(' ')] for i in f]

    safe = 0
    for i in a:
        if i == sorted(i) or i == sorted(i, reverse=True):
            i = sorted(i)
            tmp = i[0]
            for j in i[1:]:
                print(j - tmp)
                print(1 <= j - tmp <= 3)
                if 1 <= j - tmp <= 3:
                    pass
                else:
                    safe -= 1
                    break
                tmp = j
            safe += 1
    print(safe)