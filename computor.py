import sys

def check_arg(ac: int):
    if ac != 2:
        print("Wrong number of argments")
        exit()
    else:
        print("Let's have some fun with polynomial equations!")


def special_cases(str1: str, str2: str)-> bool, int:
    # prevoir un tableau genre switch ou un dico pour les msgs d erreur 
    if str1 == str2:
        print('c tout pareil')
        # cf exemple du sujet et trouver comment ca se gere (ex ici : tous les nombres réels sont une solution)
        return (False, 0)

    return (True, 1)

def parser(str1: str, str2: str):
    print(str1, str2)
    # voir exemple du sujet (meme chose des 2 cotes) et trouver les differentes exceptions possibles
    if special_cases(str1, str2) == False:
        # print le cas d erreur en fct du type d erreur (mettre un nombre qui renvoie a un msg d erreur type) 
        exit()
    # sinon trouver la puissance du cote droit et le soustraire de celui a puissance équivalente cote gauche


def main():
    av = sys.argv
    ac = len(av)

    check_arg(ac)
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre
    # + faire une str1 avec les éléments avant '=' et une str2 avec ceux après
    
    res = av[1].split('=')
    str1, str2 = res[0], res[1]
    # > une methode pour trouver directement str1 et 2 sans passer par res (= faire le split direct) ?

    parser(str1, str2)


if __name__ == "__main__":
    main()
