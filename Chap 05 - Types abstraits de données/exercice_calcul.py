from pile import *
from file import *

def expression(exp):
    pile = pileCree()
    file = fileCree()
    for char in exp:
        if char == exp[-1]:
            if char != ")":
                fileAjouterFin(file, char)
            for i in range(pileTaille(pile)):
                if pileSommet(pile) == "(":
                    pileDepiler(pile)
                else:
                    fileAjouterFin(file, pileDepiler(pile))
        if char == ")":
            for i in range(pileTaille(pile)):
                if pileSommet(pile) != ")":
                    if pileSommet(pile) == "(":
                        pileDepiler(pile)
                    else:
                        fileAjouterFin(file, pileDepiler(pile))
                else:
                    pileDepiler(pile)
                    break
        else:
            if char in ["*", "+", "-", "(", "/"]:
                pileEmpiler(pile, char)
            else:
                if char == exp[-1]:
                    return file
                fileAjouterFin(file, char)
    return file


print(expression("7-5*((9/3)-2)"))


def calcul_postfixee(exp):
    while True:
        print(exp)
        if len(exp) == 1:
            return exp[0]
        premier = exp[0]
        deuxieme = exp[1]
        troisieme = exp[2]
        if troisieme == "+":
            calcul = int(premier)+int(deuxieme)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif troisieme == "-":
            calcul = int(premier)-int(deuxieme)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif troisieme == "*":
            calcul = int(premier)*int(deuxieme)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif troisieme == "/":
            calcul = int(premier)/int(deuxieme)
            exp = exp[3:]
            exp.insert(0, calcul)


# print(calcul_postfixee(['5', '2', '*', '3', '-']))