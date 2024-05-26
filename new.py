import sys
import re
import math


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
    
    print(l, r)

    # valid1 = re.findall(r'^(-\d+(\.\d+)?\*|d+(\.d+)?\*)?X(\^d+)?$', l)
    # valid2 = re.search(r'^(-[0-9]+(\.[0-9]+)?\*|[0-9]+(\.[0-9]+)?\*)?X(\^[0-9]+)?$', r)
    # print(valid1, l, valid2, r)


    # a voir : regex a modifier ou type de recherche (findall, search, ..) a changer
    # pour eviter le 1er et le dernier element en retour (cf l et r apres regex)

    regex = "([-]?\d+\.?\d*)?\*?[Xx]\^?(\d+)*"
    l = re.findall(regex, l)
    print(l)
    r = re.findall(regex, r)
    print(r)

    d_l = {}
    d_r = {}
    tmp = {}

    for i in l:
        d_l[i[1]] = float(i[0])
    print("l=",d_l)
    for i in r:
        d_r[i[1]] = float(i[0]) * -1
    print("r=",d_r)

    for key_l in d_l.keys():
        # print("dl", key_l)
        if key_l not in d_r:
            tmp[key_l] = d_l[key_l]
        for key_r in d_r.keys():
            if key_r == key_l:
                tmp[key_l] = d_l[key_l] + d_r[key_r]

            elif key_r not in d_l:
                tmp[key_r] = d_r[key_r]
                print("tmp3",tmp)
    print(d_l, d_r, tmp)



    return (res)


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_equal(ac, av[1])

    res = parse(av[1])


    # print('Polynomial degree:', len(res)-1)
    # result(res)


if __name__ == "__main__":
    main()
