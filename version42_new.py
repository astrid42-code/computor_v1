import re


class color:
    g = '\033[92m'  # green
    y = '\033[93m'  # yellow
    r = '\033[91m'  # red
    b = '\033[94m'  # blue
    c = '\033[96m'  # cyan
    n = '\033[0m'   # grey


def equal(av: str):
    '''
    Checks if expression is valid :
    - equal sign is unique.
        returns 1 if more or less than one
    - members of the equation are valid :
        positive or negative int or float, + or -, * X^ or *,
        positive int or float
        returns 1 if not valid, 0 if valid
    Parameter:
        av (str) : av[1]
    '''

    c = av.count("=")
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        return (1)
    return (0)


def valid(left: str, right: str) -> int:
    '''
    Checks if expression is valid :
    - equal sign is unique.
        returns 1 if more or less than one
    - members of the equation are valid :
        positive or negative int or float, + or -, * X^ or *, positive int or float
        returns 1 if not valid, 0 if valid
    '''
    # regex analizing differents members of the equation
    # valid = re.search(r, '' [+/-] [int ou float] ["* X^"] [0-9*])

    res_l = re.sub("-", "+", left)
    res_l = res_l.split('+')

    res_r = re.sub("-", "+", right)
    res_r = res_r.split('+')
    if res_l[0] == '':
        res_l.remove('')
    if res_r[0] == '':
        res_r.remove('')

    for i in res_l:
        valid = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)\*?X(\^[0-9]+)?$', i)
        if valid is None:
            print(color.r + "Unvalid expression, respect this format : int/float * X^ positive int" + color.n)
            return (1)
    for i in res_r:
        if i == '0':
            continue
        valid = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)\*?X(\^[0-9]+)?$', i)
        if valid is None:
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
    left = res[0]
    right = res[1]

    if (len(right) == 0 or len(left) == 0):
        print(color.r + "Input is invalid : wrong format :(" + color.n)
        exit()
    if valid(left, right) == 1:
        exit()

    print(color.y + "Input is valid, good job :) Now, let's have some fun with polynomial equations!" + color.n)

    regex = "([-]?\d+\.?\d*)?\*?[Xx]\^?(\d+)*"
    left = re.findall(regex, left)
    right = re.findall(regex, right)

    d_l = {}
    d_r = {}
    tmp = {}

    for i in left:
        if int(i[1]) in d_l:
            d_l[int(i[1])] += float(i[0])
        else:
            d_l[int(i[1])] = float(i[0])
    for i in right:
        if int(i[1]) in d_r:
            d_r[int(i[1])] += float(i[0]) * -1
        else:
            d_r[int(i[1])] = float(i[0]) * -1

    for key_l in d_l.keys():
        if key_l not in d_r:
            tmp[key_l] = d_l[key_l]
        for key_r in d_r.keys():
            if key_r == key_l:
                tmp[key_l] = d_l[key_l] + d_r[key_r]

            elif key_r not in d_l:
                tmp[key_r] = d_r[key_r]

    # ordered dict for reduced form
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
        if v >= 0 and k is not min(s.keys()):
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
    print(color.g + 'Reduced form: ' + color.n, f'{res} = 0', sep='')


def ft_sqrt(n: int):
    if n < 0:
        n * -1
    x = n
    y = 1
    while (x - y > 0.000001):
        x = (x + y) / 2
        y = n / x
    return (x)


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
        print(color.b + 'The solution is :\n' + color.n, '{0:.5f}'.format(z), sep='')
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

        if c == 0:
            b = v[1]
            z = -a / b
            print(color.b + 'The solution is :\n' + color.n, '{0:.5f}'.format(z), sep='')
            exit()
        
        # https://www.maths-et-tiques.fr/telech/20Poly.pdf
        print(color.c + 'Discriminant calculation with discriminant = (b ** 2) - (4 * c * a):' + color.n)
        print('d = (', b, ' ** 2) - (4 * ', c, ' * ', a, ')', sep='')
        discriminant = (b ** 2) - (4 * c * a)
        print('d =', discriminant)

        if discriminant > 0:
            # z1 = -b-√discriminant / 2a and z2 = -b+√discriminant / 2a
            z1 = (-b - ft_sqrt(discriminant)) / (2 * c)
            z2 = (-b + ft_sqrt(discriminant)) / (2 * c)
            print(color.c + 'Discriminant is strictly positive, formulas are : ')
            print('z1 = -b-√discriminant / 2a and z2 = -b+√discriminant / 2a' + color.n)
            print('z1 = {0:.5f}'.format(z1), '\nz2 = {0:.5f}'.format(z2), sep='')
            print(color.c + 'The two solutions are:\n' + color.n, '{0:.5f}'.format(z1), '\n{0:.5f}'.format(z2), sep='')
        elif discriminant == 0:
            z0 = -(b / (2 * c))
            print(color.c + 'Discriminant is 0. The solution is:\n' + color.n, z0, sep='')
        elif discriminant < 0:
            # imaginary numbers solutions:
            discriminant *= -1  # absolute value of discriminant 
            # real part
            x = -b / (2 * c)
            # imaginary part
            y1 = - ft_sqrt(discriminant) / (2 * c)
            y2 = ft_sqrt(discriminant) / (2 * c)
            print(color.c + 'Discriminant is strictly negative, that implies imaginary numbers with formulas : ')
            print('real part : x = -b / (2 * c)')
            print('imaginary part : y1 = -√discriminant / 2a and y2 = √discriminant / 2a' + color.n)
            print('x = {0:.5f}'.format(x), '\ny1 = {0:.5f}'.format(y1),'\ny2 = {0:.5f}'.format(y2), sep='')
            print(color.c + 'The two solutions are:\n' + color.n, '{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y1), '\n{0:.5f}'.format(x), ' + i * {0:.5f}'.format(y2), sep='')
