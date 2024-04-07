import sys, re

def check_arg(ac: int, av: str):
    if ac != 2:
        print("Wrong number of arguments")
        exit()
    c = av.count("=") # faire une variable dans une classe pour mettre a true ou false la validite de l equation?
    if c != 1:
        print("There must be at least one equal sign, no more, no less!")
        exit()
    else:
        print("Let's have some fun with polynomial equations!")


def special_cases(str1: str, str2: str): #-> bool, int:
    # prevoir un tableau genre switch ou un dico pour les msgs d erreur 
    if str1 == str2:
        print('c tout pareil')
        # cf exemple du sujet et trouver comment ca se gere (ex ici : tous les nombres réels sont une solution)
        return (False, 0)

    return (True, 1)

def parser(str1: str, str2: str):
    print(str1, str2)
    
    # 1 verifier et stocker les elements de str1 et 2


    # 2 special_cases : voir exemple du sujet (meme chose des 2 cotes) et trouver les differentes exceptions possibles
    if special_cases(str1, str2) == False:
        # print le cas d erreur en fct du type d erreur (mettre un nombre qui renvoie a un msg d erreur type) 
        exit()
    # sinon trouver la puissance du cote droit et le soustraire de celui a puissance équivalente cote gauche


def main():
    av = sys.argv
    ac = len(av)

    check_arg(ac, av[1])
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre
    # + faire une str1 avec les éléments avant '=' et une str2 avec ceux après
    
    res = av[1].split('=')
    res[0] = re.sub(" ", "", res[0])
    res[1] = re.sub(" ", "", res[1])
    str1, str2 = res[0], res[1]

    if len(str1) == 0 or len(str2) == 0 :
        print(" You need element on both side of equal sign")
        exit()

    # > une methode pour trouver directement str1 et 2 sans passer par res (= faire le split direct) ?

    parser(str1, str2)


if __name__ == "__main__":
    main()
