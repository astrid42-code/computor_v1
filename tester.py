from new import equal, parse, reduced, result
import sys
import re
import math

# using the tester, means you have to comment main in new.py

av = sys.argv
ac = len(av)

if ac != 2:
    print("Wrong number of arguments")
    exit()
else:
    print("Welcome in computorv1!\nInput is :", av[1])

# equal check
if equal(av[1]) == 1:
    exit()

# sort : dico des elements
sort = parse(av[1])

l_k = [k for k in sort.keys()]
l_v = [int(v) if v.is_integer() else round(v, 1) for v in sort.values() ]


# reduced fct :
reduced(sort, av[1])

# degree :
degree = max(sort.keys())
if float(degree) > 2:
    print('The polynomial degree is strictly greater than 2, I can\'t solve.')

print('Polynomial degree:', degree)


# result
result(l_k, l_v, degree)