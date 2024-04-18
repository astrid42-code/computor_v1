import sys, re

def check_arg(ac: int, av: str):
    
    c = av.count("=") # faire une variable dans une classe pour mettre a true ou false la validite de l equation?
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
    d={43: '$+', 45: '$-', 61: '$'}
    res = res.translate(d).split('$')

    # extract coeff for each term of the list
    # > retirer tout ce qui est a partir du '*'
    # > si c est + en premier, le retirer; si c est - le garder
    # les garder dans une liste
    for i in range(len(res)):
        # Séparation de la chaîne en fonction de '*'
        c = res[i].split('*')
        if (len(c) > 1):
            if c[0][0] == '+':
                c = c[0][1::]
                res[i] = float(c)
            # Remplacement de l'élément par la partie avant '*'
            else:
                res[i] = float(c[0])

    # substract 1st term and last term :
    # res[0] -= res[len(res)-1] # possible, mais necessite ensuite de remove le dernier element de la liste
    res[0] -= res.pop() #  pour recuperer le dernier element de la liste et le retirer directement

    
    # retransformer av avec 1er terme = c[0] mais pb des float/int > trouver la fct qui trouve si c int (x.0) ou float (x.8)
    c = 0
    for i in res:
        if i.is_integer():
            res[c] = int(i)
        c += 1
    
    i, j = 0, 0
    while (av[i] != '*'):
        i += 1
    while (av[j] != '='):
        j+=1   
    red = av[i-1:j]
    # puis recopier tout ce qui est a partir du '*' jusqu au '='
    print(f'Reduced form: {res[0]}{red} = 0')

    return(res)


def result(res):
    print("yeah")
    # faire 4 cas en fct du degre : 0, 1, 2, tout le reste

def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_arg(ac, av[1])
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre

    res=parse(av[1])

    print('Polynomial degree:', len(res)-1)
    result(res)


if __name__ == "__main__":
    main()
