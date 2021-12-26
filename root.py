from math import pow
from sys import argv, exit

if len(argv) not in [4, 3]:                     # If parameters are fewer than 2 and more than 3
    print("You should pass 2 or 3 parameters")
    exit()

num = int(argv[1])
grid = int(argv[2])

try:                                            # If user does not pass decimals parameter
    decimals = int(argv[3])
except IndexError:
    decimals = 1

def root(num, grid, decimals):
    checks = []
    i = 0                                       # Itering variable
    coefficient=1
    final=0
    current_decimal = -1                        # Number of current calculating decimal (-1)

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
        print(round((-1)*root((-1)*num, grid, decimals), decimals))
elif num>0:
    print(round(root(num, grid, decimals), decimals))
else:
    print(0)
