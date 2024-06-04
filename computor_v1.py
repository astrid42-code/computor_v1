import sys
from parse import check_equal, parse
from reduced import reduced
from calculation import result


def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_equal(ac, av[1])

    # sort : dico des elements
    sort = parse(av[1])

    l_k = [k for k in sort.keys()]
    l_v = [int(v) if v.is_integer() else round(v, 1) for v in sort.values() ]

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
