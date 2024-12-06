if __name__ == '__main__':
    f = open('6.in', 'r').read()[:-1].split('\n')

    total = 0
    for l in range(len(f)):
        for m in range(len(f[0])):
            print(l, m)
            a = f.copy()
            if a[l][m] == '#':
                continue
            a[l] = a[l][:m] + '#' + a[l][m + 1:]
            z = [[[''] for z in x] for x in a]
            k = 0
            j = 0
            for i in f:
                if '^' in i:
                    j = i.index('^')
                    k = f.index(i)
                    break
            d = 'up'
            while 0 <= k < len(a[0]) and 0 <= j < len(a):
                a[k] = a[k][:j] + 'X' + a[k][j + 1:]
                if d in z[k][j]:
                    total += 1
                    break
                z[k][j].append(d)
                if d == 'left':
                    if j - 1  < 0:
                        break
                    if a[k][j - 1] == '#':
                        d = 'up'
                    else:
                        j -= 1
                elif d == 'down':
                    if k + 1 >= len(a):
                        break
                    if a[k + 1][j] == '#':
                        d = 'left'
                    else:
                        k += 1
                elif d == 'right':
                    if j + 1 >= len(a[0]):
                        break
                    if a[k][j + 1] == '#':
                        d = 'down'
                    else:
                        j += 1
                else:
                    if k - 1 < 0:
                        break
                    if a[k - 1][j] == '#':
                        d = 'right'
                    else:
                        k -= 1

    print(total)