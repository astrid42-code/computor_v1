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


def special_cases(left: str, right: str): #-> bool, int:
    # prevoir un tableau genre switch ou un dico pour les msgs d erreur 
    if left == right:
        print('c tout pareil')
        # cf exemple du sujet et trouver comment ca se gere (ex ici : tous les nombres réels sont une solution)
        return (False, 0)

    return (True, 1)

def parser(left: str, right: str):
    print(left, right)
    
    # 1 verifier et stocker les elements de left et right
    d1, d2 = {}, {}
    
    # right part
    res = right.split('*')
    
    d2[res[0]] = res[1][2:]

    print(res, d2)

    mais comment ca se passe quand plsrs elements en right (a faire avec left )

    + verifier que chaque membre existe bien (ex la cle ou la value ne sont pas nulles) sinon msg erreur et exit 
    > check qu il y a bien X^, et les valeurs
    > a faire dans une boucle ou - et + sont a conserver (enfin surtout le - s il y a !!) 
    et servent de separateurs pour remplir le dico et verifier que tous les elements sont bien la dans chaque morceau


    # 2 special_cases : voir exemple du sujet (meme chose des 2 cotes) et trouver les differentes exceptions possibles
    if special_cases(left, right) == False:
        # print le cas d erreur en fct du type d erreur (mettre un nombre qui renvoie a un msg d erreur type) 
        exit()
    # sinon trouver la puissance du cote droit et le soustraire de celui a puissance équivalente cote gauche


def main():
    av = sys.argv
    ac = len(av)

    check_arg(ac, av[1])
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre
    # + faire une string left avec les éléments avant '=' et une string right avec ceux après
    
    res = av[1].split('=')
    res[0] = re.sub(" ", "", res[0])
    res[1] = re.sub(" ", "", res[1])
    left, right = res[0], res[1]

    if len(left) == 0 or len(right) == 0 :
        print(" You need element on both side of equal sign")
        exit()

    # > une methode pour trouver directement left et right sans passer par res (= faire le split direct) ?

    parser(left, right)


if __name__ == "__main__":
    main()
