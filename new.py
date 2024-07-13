import sys
import re
import math


def equal(av: str):
    '''
    Checks if expression is valid :
    - equal sign is unique.
        returns 1 if more or less than one
    - members of the equation are valid :
        positive or negative int or float, + or -, * X^ or *, positive int or float
        returns 1 if not valid, 0 if valid
    Parameter:
        av (str) : av[1] 
    '''

    c = av.count("=")
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        return (1)
    return (0)

def valid(l: str, r: str) -> int:
    '''
    Checks if expression is valid :
    - equal sign is unique.
        returns 1 if more or less than one
    - members of the equation are valid :
        positive or negative int or float, + or -, * X^ or *, positive int or float
        returns 1 if not valid, 0 if valid
    '''
    # faire regex analysant les differents membres de l'equation
    # valid = re.search( [+/-] [int ou float] ["* X^"] [0-9])
    # if valid == NONE:
    #     print("Unvalid expression, respect this format : int/float * X^ positive int")
    #     return (1)
    return (0)

def parse(av: str):
    '''
    Parses av[1]: 
        - checks format
        - creates 2 lists for left and right members of the equation
        - creates a temp dictionnary with both left and right members 
          where keys = powers and value = coeffs

    Returns a sorted dictionnary (sorted by keys)
    '''

    # list of the equation terms
    res = re.sub(" ", "", av)
    # https://favtutor.com/blogs/replace-multiple-characters-in-string-python
    # https://www.w3schools.com/python/ref_string_translate.asp

    res = res.split('=')
    l = res[0]
    r = res[1]
    if (len(r) == 0 or len(l) == 0):
        print("Input is invalid : wrong format :(")
        exit()
    if valid(l, r) == 1:
        exit()
    
    print(l, r)

    # autres checks a faire pour valider l input : nombres et pas de lettres autres que X, 
    # check pour signes * + - et ^
    # et autres? ex : si un des deux termes est juste 0, devrait etre ok?
    # (print les listes pour voir si ce sont bien des float en values)
    # comment checker la validite de l input en general de facon simple? (voir le regex de Louis!!!)
    
    print("Input is valid, good job :) Now, let's have some fun with polynomial equations!")

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
    '''
    Creates a string with keys and volues of the dictionnary
    to print the reduced form of the equation.
    Parameters:
        - s (dict): dictionnary with powers (keys) abd coeffs(values)
        - av (str): av[1]

    Example of output :
    4 * X^0 + 2 * X^1 + 1 * X^2 = 0
    '''
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


def result(k: list, v: list, degree: int):
    '''
    Computes equation
    Parameters:
        - k, v (list): lists ok keys (powers) and values (coefficients)
        - degree (int): compute degree
    
    
    '''
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
            # imaginary numbers solutions:
            discriminant *= -1  # valeur absolue du discriminant (car pas de racine carree d un nbr negatif)
            # partie reelle
            x = -b / (2 * c) 
            # parties imaginaires
            y1 = - math.sqrt(discriminant) / (2 * c)
            y2 = math.sqrt(discriminant) / (2 * c)
            print('Discriminant is strictly negative, the two solutions are:\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y1), '\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y2), sep='')


# def main():
#     av = sys.argv
#     ac = len(av)

#     if ac != 2:
#         print("Wrong number of arguments")
#         exit()

#   equal check
    # if equal(av[1]) == 1:
    #     exit()

#     # sort : dico des elements
#     sort = parse(av[1])

#     l_k = [k for k in sort.keys()]
#     l_v = [int(v) if v.is_integer() else round(v, 1) for v in sort.values() ]

#     # reduced fct :
#     reduced(sort, av[1])

#     # degree :
#     degree = max(sort.keys())
#     if float(degree) > 2:
#         print('The polynomial degree is strictly greater than 2, I can\'t solve.')

#     print('Polynomial degree:', degree)


#     # result
#     result(l_k, l_v, degree)


# if __name__ == "__main__":
#     main()


# nombres imqginaires :
# Le carré d'un nombre imaginaire pur est un nombre réel négatif 
# ou nul, et les racines carrées d'un nombre réel négatif sont des imaginaires purs. 