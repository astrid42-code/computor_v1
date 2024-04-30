import sys
import re
import math


def check_arg(ac: int, av: str):
    c = av.count("=")
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        exit()
    else:
        print("Let's have some fun with polynomial equations!")


def parse(av: str):
    # list of the equation terms
    res = re.sub(" ", "", av)
    res = res.split('=', maxsplit=1)
    r1 = res[0]
    r2 = res[1]
    d = {43: '$+', 45: '$-'}
    r1 = r1.translate(d).split('$')
    r2 = r2.translate(d).split('$')
    print("1", r1, "2", r2)


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_arg(ac, av[1])

    res = parse(av[1])

    # print('Polynomial degree:', len(res)-1)
    # result(res)


if __name__ == "__main__":
    main()
