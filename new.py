import sys
import re
import math


def check_equal(ac: int, av: str):
    c = av.count("=")
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        exit()


def parse(av: str):
    # list of the equation terms
    res = re.sub(" ", "", av)
    # https://favtutor.com/blogs/replace-multiple-characters-in-string-python
    # https://www.w3schools.com/python/ref_string_translate.asp

    res = res.split('=')
    l = res[0]
    r = res[1]
    if (len(r) == 0 or len(l) == 0):
        print("Wrong format")
        exit()
    
    print("Let's have some fun with polynomial equations!")

    regex = "([-]?\d+\.?\d*)?\*?[Xx]\^?(\d+)*"
    l = re.findall(regex, l)
    r = re.findall(regex, r)

    d_l = {}
    d_r = {}
    tmp = {}

    for i in l:
        d_l[int(i[1])] = float(i[0])
    for i in r:
        d_r[int(i[1])] = float(i[0]) * -1

    for key_l in d_l.keys():
        if key_l not in d_r:
            tmp[key_l] = d_l[key_l]
        for key_r in d_r.keys():
            if key_r == key_l:
                tmp[key_l] = d_l[key_l] + d_r[key_r]

            elif key_r not in d_l:
                tmp[key_r] = d_r[key_r]

    # ordonner le dico pour affichage reduced
    s = dict(sorted(tmp.items()))

    return (s)


def reduced(s: dict, av: str):
    red = av[av.find('*'):av.find('^')]
    res = ''

    for k, v in s.items():
        if v > 0 and k is not min(s.keys()) :
            res += ' + '
        if v.is_integer():
            s[k] = int(v)
        else:
            s[k] = round(v, 1)
        if v < 0:
            res += ' - ' + str(s[k] * -1) + red + '^' + str(k)
            s[k] = v * -1
        else:
            res += str(s[k]) + ' ' + red + '^' + str(k)
    print(f'Reduced form: {res} = 0')
    return (s)


def result(k: list, v: list, degree: int):
    a = v[0]
    if degree == 0:
        if a == 0:
            print('There is infinite solutions')
        else:
            print('There is no solution')
    elif degree == 1:
        b = v[1]
        z = -a / b
        print('The solution is :\n', z, sep='')
    elif degree == 2:
        if len(k) == 3:
            b = v[1]
            c = v[2]
        elif len(k) == 2:
            c = v[1]
            if k[0] == 0:
                b = 0
            elif k[0] == 1:
                b = v[0]
                a = 0
        elif len(k) == 1:
            c = v[0]
            a = 0
            b = 0
        # https://www.maths-et-tiques.fr/telech/20Poly.pdf
        discriminant = (b ** 2) - (4 * c * a)

        if discriminant > 0:
            z1 = (-b - math.sqrt(discriminant)) / (2 * c) # z1 = -b-√discriminant / 2a
            z2 = (-b + math.sqrt(discriminant)) / (2 * c) # z2 = -b+√discriminant / 2a
            print('Discriminant is strictly positive, the two solutions are:\n{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
        elif discriminant == 0:
            z0 = -(b / (2 * c))
            print('The solution is:\n', z0)
        elif discriminant < 0:
            # imaginary numbres solutions:
            discriminant *= -1  # valeur absolue du discriminant (car pas de racine carree d un nbr negatif)
            # partie reelle
            x = -b / (2 * c) 
            # parties imaginaires
            y1 = - math.sqrt(discriminant) / (2 * c)
            y2 = math.sqrt(discriminant) / (2 * c)
            print('Discriminant is strictly negative, the two solutions are:\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y1), '\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y2), sep='')


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_equal(ac, av[1])

    # sort : dico des elements
    sort = parse(av[1])

    l_k = [k for k in sort.keys()]
    l_v = [int(v) if v.is_integer() else round(v, 1) for v in sort.values() ]
    # print(l_k, l_v)

    # reduced fct :
    s = reduced(sort, av[1])

    # degree :
    degree = max(sort.keys())
    if float(degree) > 2:
        print('The polynomial degree is strictly greater than 2, I can\'t solve.')

    print('Polynomial degree:', degree)


    # result(res)
    result(l_k, l_v, degree)


if __name__ == "__main__":
    main()


# nombres imqginaires :
# Le carré d'un nombre imaginaire pur est un nombre réel négatif 
# ou nul, et les racines carrées d'un nombre réel négatif sont des imaginaires purs. 