if __name__ == '__main__':
    f = open('6.in', 'r').read()[:-1].split('\n')
    a = [i for i in f]
    k = 0
    j = 0
    for i in f:
        if '^' in i:
            j = i.index('^')
            k = f.index(i)
            break
    d = 'up'
    while 0 <= k < len(f[0]) and 0 <= j < len(f):
        f[k] = f[k][:j] + 'X' + f[k][j + 1:]

        print(k, j)
        if d == 'left':
            if j - 1  < 0:
                break
            if f[k][j - 1] == '#':
                d = 'up'
            else:
                j -= 1
        elif d == 'down':
            if k + 1 >= len(f):
                break
            if f[k + 1][j] == '#':
                d = 'left'
            else:
                k += 1
        elif d == 'right':
            if j + 1 >= len(f[0]):
                break
            if f[k][j + 1] == '#':
                d = 'down'
            else:
                j += 1
        else:
            if k - 1 < 0:
                break
            if f[k - 1][j] == '#':
                d = 'right'
            else:
                k -= 1
    total = 0
    for i in f:
        total += i.count('X')
    print(f)
    print(total)