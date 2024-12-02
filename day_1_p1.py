import re

if __name__ == '__main__':
    f = open('input1.txt', 'r').read().split('\n')
    a = sorted([int(i.split('   ')[0]) for i in f])
    b = sorted([int(i.split('   ')[1]) for i in f])
    print(a)
    print(b)
    d = [abs(b[i]- a[i]) for i in range(len(a))]
    print(d)
    print(sum(d))