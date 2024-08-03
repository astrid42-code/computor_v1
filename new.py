import sys
import re
import math


class color:
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    r = '\033[91m' # rouge
    b = '\033[94m' # blue
    c = '\033[96m' # cyan
    n = '\033[0m' #gris, couleur normale


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
    # valid = re.search(r, '' [+/-] [int ou float] ["* X^"] [0-9*])

    res_l = re.sub("-", "+", l)
    res_l = res_l.split('+')

    res_r = re.sub("-", "+", r)
    res_r = res_r.split('+')
    if res_l[0] == '':
        res_l.remove('')
    if res_r[0] == '':
        res_r.remove('')  

    # print(res_l, res_r)
    for i in res_l:
        valid = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)?\*?X(\^[0-9]+)?$', i)
        # print(valid)
        if valid == None:
            print(color.r + "Unvalid expression, respect this format : int/float * X^ positive int" + color.n)
            return (1)
    for i in res_r:
        if i == '0':
            continue
        valid = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)?\*?X(\^[0-9]+)?$', i)
        # print(valid)
        if valid == None:
            print(color.r + "Unvalid expression, respect this format : int/float * X^ positive int" + color.n)
            return (1)
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
        print(color.r + "Input is invalid : wrong format :(" + color.n)
        exit()
    if valid(l, r) == 1:
        exit()

    print(color.y + "Input is valid, good job :) Now, let's have some fun with polynomial equations!" + color.n)

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
    print(color.g + 'Reduced form: ' + color.n, f'{res} = 0' )


# def ft_sqrt(int n):


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
            print(color.c + 'There is infinite solutions, any real number is a solution' + color.n)
        else:
            print(color.c + 'There is no solution' + color.n)
    elif degree == 1:
        b = v[1]
        z = -a / b
        print(color.b + 'The solution is :\n' + color.n, z, sep='')
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
        print(color.c + 'Discriminant calculation with discriminant = (b ** 2) - (4 * c * a):' + color.n)
        print('d = (', b, ' ** 2) - (4 * ', c, ' * ', a, ')', sep='')
        discriminant = (b ** 2) - (4 * c * a)
        print('d =', discriminant)

# faire une fonction pour remplacer math.sqrt!

        if discriminant > 0:
            z1 = (-b - math.sqrt(discriminant)) / (2 * c) # z1 = -b-√discriminant / 2a
            z2 = (-b + math.sqrt(discriminant)) / (2 * c) # z2 = -b+√discriminant / 2a
            print(color.c + 'Discriminant is strictly positive, formulas are : ')
            print('z1 = -b-√discriminant / 2a and z2 = -b+√discriminant / 2a' + color.n)
            print('z1 = ', z1,'\nz2 = ', z2, sep='')
            print(color.c + 'The two solutions are:\n' + color.n, '{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
        elif discriminant == 0:
            z0 = -(b / (2 * c))
            print(color.c + 'Discriminant is 0. The solution is:\n' + color.n, z0, sep='')
        elif discriminant < 0:
            # imaginary numbers solutions:
            discriminant *= -1  # valeur absolue du discriminant (car pas de racine carree d un nbr negatif)
            # partie reelle
            x = -b / (2 * c) 
            # parties imaginaires
            y1 = - math.sqrt(discriminant) / (2 * c)
            y2 = math.sqrt(discriminant) / (2 * c)
            print(color.c + 'Discriminant is strictly negative, that implies imaginary numbers with formulas : ')
            print('real part : x = -b / (2 * c)')
            print('imaginary part : y1 = -√discriminant / 2a and y2 = √discriminant / 2a' + color.n)
            print('x = {0:.5f}'.format(x), '\ny1 = {0:.5f}'.format(y1),'\ny2 = {0:.5f}'.format(y2), sep='')
            print(color.c + 'The two solutions are:\n' + color.n, '{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y1), '\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y2), sep='')


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