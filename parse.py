import re
import math

# checker =
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

