import re

r = "mul\((\d*),(\d*)\)"
r1 = "do()"
r2 = "don't()"
cando = True

if __name__ == '__main__':
    a = open('3.in', 'r').read()

    x = 0
    y = a.index(r2)
    t = 0

    while True:
        z = a[x:y]
        b = re.findall(r, z)
        for i, j in b:
            t += int(i)*int(j)

        try:
            x = a[y:].index(r1) + y
        except ValueError:
            break
        if a[x:].index(r2) is None:
            break
        y = a[x:].index(r2) + x

    print(t)
