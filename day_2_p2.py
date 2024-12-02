import re

if __name__ == '__main__':
    f = open('input2.txt', 'r').read().split('\n')
    a = [[int(j) for j in i.split(' ')] for i in f]

    safe = 0
    for k in a:
        if k == sorted(k) or k == sorted(k, reverse=True):
            k = sorted(k)
            tmp = k[0]
            for j in k[1:]:
                if 1 <= j - tmp <= 3:
                    pass
                else:
                    break
                tmp = j
            else:
                safe += 1
                continue
        s = False
        for b in range(len(k)+1):
            if s:
                safe += 1
                break
            i = [x for i,x in enumerate(k) if i != b]
            if i == sorted(i) or i == sorted(i, reverse=True):
                i = sorted(i)

                tmp = i[0]
                for j in i[1:]:
                    if 1 <= j - tmp <= 3:
                        pass
                    else:
                        break
                    tmp = j
                else:
                    s = True
                    continue
    print(safe)