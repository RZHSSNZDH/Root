from math import *
from sys import argv

num = int(argv[1])
grid = int(argv[2])
decimals = int(argv[3])

def root(num, grid, decimals=1):
    checks = []
    i = 0
    coefficient=1
    final=0
    current_decimal = -1

    while current_decimal!=decimals:
        if pow((final+coefficient*i), grid)>num and i not in checks:
            final += coefficient*checks[-1]
            coefficient = coefficient/10
            checks.clear()
            i = 0
            current_decimal += 1

        elif pow((final+coefficient*i),grid)<num and i not in checks:
            checks.append(i)
            i += 1

        else:
            final += coefficient*i
            coefficient = coefficient/10
            checks.clear()
            i = 0
            current_decimal += 1

    return final

if num<0:
    if grid%2==0:
        print("Negative number can't have even grid")
    else:
        print((-1)*root((-1)*num, grid, decimals))
elif num>0:
    print(root(num, grid, decimals))
else:
    print(0)
