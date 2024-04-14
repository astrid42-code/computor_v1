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


    # substract 1st term and last term :
    # c[0] -= c[len(c)-1] # ou c.pop() pour recuperer le dernier element de la liste

    
    # retransformer av avec 1er terme = c[0] 
    # puis recopier tout ce qui est a partir du '*' jusqu au '='
    # + ecrire '0' final
    # + verifier presence des spaces

    print(res)

def main():
    av = sys.argv
    ac = len(av)

    if ac != 2:
        print("Wrong number of arguments")
        exit()

    check_arg(ac, av[1])
    
    # avant parsing : 
    # - découper la str pour avoir les differents éléments de l expression dans l ordre

    parse(av[1])



if __name__ == "__main__":
    main()
