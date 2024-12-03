import re
r = "mul\((\d*),(\d*)\)"

if __name__ == '__main__':
    a = open('3.in', 'r').read()
    b = re.findall(r, a)
    t = 0
    for i, j in b:
        t += int(i)*int(j)
    print(t)
