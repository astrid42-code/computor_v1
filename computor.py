import sys

def check_arg(ac: int):
    if ac != 2:
        print("Wrong number of argments")
        exit()
    else:
        print("Let's have fun with some polynomial equations!")

def special_cases():


def parser(av: str):
    print(av)
    # voir exemple du sujet (meme chose des 2 cotes) et trouver les differentes exceptions possibles
        # special_cases()
    # sinon trouver la puissance du cote droit et le soustraire de celui a puissance équivalente cote gauche


def main():
    av = sys.argv
    ac = len(av)

    check_arg(ac)
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre
    # + faire une str1 avec les éléments avant '=' et une str2 avec ceux après

    parser(av[1])


if __name__ == "__main__":
    main()
