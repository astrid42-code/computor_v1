from new import equal, parse, reduced, result
import sys
import re


class color:
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    r = '\033[91m' # rouge
    b = '\033[94m' # blue
    c = '\033[96m' # cyan
    n = '\033[0m' #gris, couleur normale

# using the tester, means you have to comment main in new.py

av = sys.argv
ac = len(av)

if ac != 2:
    print("Wrong number of arguments")
    exit()
else:
    print(color.b + "Welcome in computorv1!" + color.n, color.g + "\nInput is :" + color.n, av[1])

# equal check
if equal(av[1]) == 1:
    exit()

# sort : dico des elements
sort = parse(av[1])
#print("sort=", sort)

l_k = [k for k in sort.keys()]
l_v = [int(v) if v.is_integer() else round(v, 1) for v in sort.values() ]

# reduced fct :
reduced(sort, av[1])

# degree :
degree = max(sort.keys())
print(color.g + 'Polynomial degree:' + color.n, degree)
if float(degree) > 2:
    print(color.r + 'The polynomial degree is strictly greater than 2, I can\'t solve.' + color.n)



# result
result(l_k, l_v, degree)