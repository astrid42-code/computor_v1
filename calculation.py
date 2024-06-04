import math


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

