from pile import *
from file import *

def calcul(exp):
    pile = pileCree()
    file = fileCree()
    for i in range(len(exp)):
        if i == len(exp)-1:
            if exp[i] != ")":
                fileAjouterFin(file, exp[i])
            for i in range(pileTaille(pile)):
                if pileSommet(pile) == "(":
                    pileDepiler(pile)
                else:
                    fileAjouterFin(file, pileDepiler(pile))
        if exp[i] == ")":
            while pileSommet(pile) != "(":
                fileAjouterFin(file, pileDepiler(pile))
            pileDepiler(pile)
        else:
            if exp[i] in ["*", "+", "-", "(", "/"]:
                pileEmpiler(pile, exp[i])
            else:
                if exp[i] == exp[-1]:
                    return file
                fileAjouterFin(file, exp[i])
    return file

def postfix(exp):
    for i in range(len(exp)):
        if exp[i] in ["+", "*", "-", "/"]:
            operande1 = exp[i-2]
            operande2 = exp[i-1]
            operateur = exp[i]
        if operateur == "+":
            calcul = int(operande1)+int(operande2)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif operateur == "-":
            calcul = int(operande1)-int(operande2)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif operateur == "*":
            calcul = int(operande1)*int(operande2)
            exp = exp[3:]
            exp.insert(0, calcul)
        elif operateur == "/":
            calcul = int(operande1)/int(operande2)
            exp = exp[3:]
            exp.insert(0, calcul)