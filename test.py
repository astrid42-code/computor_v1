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
    d = {43: '$', 45: '$-', 61: '$='}
    res = res.translate(d).split('$')
    s = len(res)
    i = 0
    while (i < s):
        # print(i, l, res[i])
        if res[i] == "=":
            del res[i]
            s -= 1
            i -= 1
        i += 1
    print(res)
    
    
    
    
    # for i in range(l):
    #     valid = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)?X(\^[0-9]+)?$', res[i])
    #     print(valid)
    return (res)


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
