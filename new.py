import sys
import re
import math
# from decimal import *


def check_equal(ac: int, av: str):
    c = av.count("=")  # faire une variable dans une classe pour mettre a true ou false la validite de l equation?
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        exit()


def parse(av: str):
    # list of the equation terms
    res = re.sub(" ", "", av)
    # print("res1=", res)
    # https://favtutor.com/blogs/replace-multiple-characters-in-string-python
    # https://www.w3schools.com/python/ref_string_translate.asp

    res = res.split('=')
    l = res[0]
    r = res[1]
    if (len(r) == 0 or len(l) == 0):
        print("Wrong format")
        exit()
    
    print("Let's have some fun with polynomial equations!")
    
    # print(l, r)

    # valid1 = re.findall(r'^(-\d+(\.\d+)?\*|d+(\.d+)?\*)?X(\^d+)?$', l)
    # valid2 = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)?X(\^[0-9]+)?$', r)
    # print(valid1, l, valid2, r)


    # a voir : regex a modifier ou type de recherche (findall, search, ..) a changer
    # pour eviter le 1er et le dernier element en retour (cf l et r apres regex)

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
    # print(s)
    red = av[av.find('*'):av.find('^')]
    res = ''
    # imprimer l equation en recuperant les keys pour les puissances et les values pour les coeff

    for k, v in s.items():
        # print('1', s)
        if v > 0 and k is not min(s.keys()) :
            res += ' + '
        if v.is_integer():
            s[k] = int(v)
        else:
            s[k] = round(v, 1)  # arrondir a un chiffre apres la virgule
        # print('2', s)
        if v < 0:
            res += ' - ' + str(s[k] * -1) + red + '^' + str(k)
            s[k] = v * -1
            # res += str(s[k])
        # print(res)
        else:
            res += str(s[k]) + ' ' + red + '^' + str(k)
        # print(res)
    print(f'Reduced form: {res} = 0')
    return (s)


# def result(res):
#     # faire 4 cas en fct du degre : 0, 1, 2, tout le reste
#     a = res[0]
#     if len(res) > 1:
#         b = res[1]
#     if len(res) == 1:  # http://serge.mehl.free.fr/anx/equ1.html
#         if a == 0:
#             print('There is infinite solutions')
#         else:
#             print('There is no solution')
#     elif len(res) == 2:  # 1st degree : http://serge.mehl.free.fr/anx/equ1.html
#         z = -a / b
#         print('The solution is :\n', z, sep='')
#     elif len(res) == 3:  # 2nd degree
#         # b = res[1]
#         c = res[2]
#         # https://www.maths-et-tiques.fr/telech/20Poly.pdf
#         discriminant = (b ** 2) - (4 * c * a)
#         # print(discriminant)
#         if discriminant > 0:
#             z1 = (-b - math.sqrt(discriminant)) / (2 * c) # z1 = -b-√discriminant / 2a
#             z2 = (-b + math.sqrt(discriminant)) / (2 * c) # z2 = -b+√discriminant / 2a
#             print('Discriminant is strictly positive, the two solutions are:\n{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
#         elif discriminant == 0:
#             z0 = -(b / (2 * c))
#             print('The solution is:\n', z0)
#         elif discriminant < 0:
#             print('No real solution, discriminant is strictly negative :', discriminant)


def result(k: list, v: list, degree: int):
    # print(k, v, degree)
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
        # print(discriminant)
        if discriminant > 0:
            z1 = (-b - math.sqrt(discriminant)) / (2 * c) # z1 = -b-√discriminant / 2a
            z2 = (-b + math.sqrt(discriminant)) / (2 * c) # z2 = -b+√discriminant / 2a
            print('Discriminant is strictly positive, the two solutions are:\n{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
        elif discriminant == 0:
            z0 = -(b / (2 * c))
            print('The solution is:\n', z0)
        elif discriminant < 0:
            print('No real solution, discriminant is strictly negative :', discriminant)

    # elif len(v) == 2:  # 1st degree : http://serge.mehl.free.fr/anx/equ1.html
    #     z = -c / b
    #     print('The solution is :\n', z, sep='')
    # elif len(v) == 3:  # 2nd degree
    #     a = v[2]
    #     # https://www.maths-et-tiques.fr/telech/20Poly.pdf
    #     discriminant = (b ** 2) - (4 * a * c)
    #     print(discriminant)
    #     if discriminant > 0:
    #         z1 = (-b - math.sqrt(discriminant)) / (2 * a) # z1 = -b-√discriminant / 2a
    #         z2 = (-b + math.sqrt(discriminant)) / (2 * a) # z2 = -b+√discriminant / 2a
    #         print('Discriminant is strictly positive, the two solutions are:\n{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
    #     elif discriminant == 0:
    #         z0 = -(b / (2 * a))
    #         print('The solution is:\n', z0)
    #     elif discriminant < 0:
    #         print('No real solution, discriminant is strictly negative :', discriminant)


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_equal(ac, av[1])

    # res = liste des elements de l equation
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
