import sys
import re
import math


def check_arg(ac: int, av: str):
    c = av.count("=")  # faire une variable dans une classe pour mettre a true ou false la validite de l equation?
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        exit()
    else:
        print("Let's have some fun with polynomial equations!")


def parse(av: str):
    # list of the equation terms
    res = re.sub(" ", "", av)
    # https://favtutor.com/blogs/replace-multiple-characters-in-string-python
    # https://www.w3schools.com/python/ref_string_translate.asp
    d = {43: '$+', 45: '$-', 61: '$'}
    res = res.translate(d).split('$')

    # extract coeff for each term of the list
    # > retirer tout ce qui est a partir du '*'
    # > si c est + en premier, le retirer; si c est - le garder
    # les garder dans une liste
    # print('res', res)
    # coeff = []
    s = len(res)
    for i in range(s):
        # print('1', res)

        # Séparation de la chaîne en fonction de '*'
        tmp = res[i].split('*')
        # print(res[i])
        # if len(tmp) == 1:
        #     res.remove(res[i])
        #     s -= 1
        #     i -= 1

        if (len(tmp) > 1):
            if tmp[0][0] == '+':
                tmp = tmp[0][1::]
                res[i] = float(tmp)
                # coeff.append(float(tmp))
            # Remplacement de l'élément par la partie avant '*'
            else:
                res[i] = float(tmp[0])
                # coeff.append(float(tmp[0]))
    #     print('2', res)
    # print('3', res)
    # print(coeff, res)

    # substract 1st term and last term :
    # res[0] -= res[len(res)-1] # possible, mais necessite ensuite de remove le dernier element de la liste
    # print(len(res), res.pop())
    # if len(res) > 2:
    res[0] -= res.pop()  # pour recuperer le dernier element de la liste et le retirer directement

    # Souci a regler : si 1er term ou dernier sont negatifs
    # + quand 1 seul terme de chaque cote (il ne veut pas soustraire element 0 et 1)

    # retransformer av avec 1er terme = c[0] mais pb des float/int > trouver la fct qui trouve si c int (x.0) ou float (x.8)
    count = 0
    for i in res:
        if i.is_integer():
            res[count] = int(i)
        count += 1

    red = av[av.find('*'):av.find('=')]
    # puis recopier tout ce qui est a partir du '*' jusqu au '='
    print(f'Reduced form: {res[0]:g} {red} = 0')  # format :g pour un chiffre apres virgule 
    # cf https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting/

    return (res)


def result(res):
    # faire 4 cas en fct du degre : 0, 1, 2, tout le reste
    a = res[0]
    if len(res) > 1:
        b = res[1]
    if len(res) == 1:  # http://serge.mehl.free.fr/anx/equ1.html
        if a == 0:
            print('There is infinite solutions')
        else:
            print('There is no solution')
    elif len(res) == 2:  # 1st degree : http://serge.mehl.free.fr/anx/equ1.html
        z = -a / b
        print('The solution is :\n', z)
    elif len(res) == 3:  # 2nd degree
        # b = res[1]
        c = res[2]
        # https://www.maths-et-tiques.fr/telech/20Poly.pdf
        discriminant = (b ** 2) - (4 * c * a)
        # print(discriminant)
        if discriminant > 0:
            z1 = (-b - math.sqrt(discriminant)) / (2 * c) # z1 = -b-√discriminant / 2a
            z2 = (-b + math.sqrt(discriminant)) / (2 * c) # z2 = -b+√discriminant / 2a
            print('Discriminant is strictly positive, the two solutions are:\n', z1, '\n', z2)
        elif discriminant == 0:
            z0 = -(b / (2 * c))
            print('The solution is:\n', z0)
        elif discriminant < 0:
            print('No real solution, discriminant is strictly negative :', discriminant)

    elif len(res) > 3:
        print('The polynomial degree is strictly greater than 2, I can\'t solve.')


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_arg(ac, av[1])

    res = parse(av[1])

    print('Polynomial degree:', len(res)-1)
    result(res)


if __name__ == "__main__":
    main()
