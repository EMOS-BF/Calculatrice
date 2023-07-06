from fonctions.operation import *
from fonctions.check import *
from fonctions.checkOperation import *
from fonctions.sortie import sortie

print("Calculatrice console: \n")
q =1
while q == 1:

    print("Veuillez choisir une operation de base\n")
    print("Pour addition (a+b) entrez: + \n")
    print("Pour la soustration (a-b) entrez: -\n")
    print("Pour la multiplication (a*b) entrez : *\n")
    print("Pour la division (a/b) entrez: / \n")

    k = 1
    while k == 1:
        operation = str(input("Entrez l'operation SVP: "))
        if checkOperation(operation) == 0:
            print("Veuillez Entrez une operation valide\n")
            k = 1
        else :
            k = 0

    c = 1
    while (c == 1):
        a = input("Entrez un le premier nombre a: ")
        if check(a) == 0:
            print("Entrez un nombre entier SVP")
            c = 1
        else:
            c = 0
        print("")
    c = 1
    while (c == 1):
        b = input("Entrez le second nombre b: ")
        print("")
        if check(b) == 0:
            print("Entrez un nombre entier SVP")
            c = 1
        else:
            c = 0


    if operation == "+":
        print("Résultat=", addition(a,b))
    elif operation == "-":
        print("Résultat=",soustraction(a,b))
    elif operation == "*":
        print("Résultat=",multiplication(a,b))
    elif operation == "/":
        if division(a,b) == "a":
            print("Impossible de diviser par 0\n")
        else:
            print("Résultat=",division(a,b))
    reponse = input("Voulez vous faire une autre operation\n entrez 'oui' ou 'non' comme reponse: \n")
    resValable=0 # permet de voir si la réponse de l'utilisateur est valable
    while resValable ==0:
        if reponse.lower() == "oui":
            q =1
            resValable=1
        elif reponse.lower() == "non":
            sortie()
            resValable=1
        else:
            reponse = input("Veuillez repondre à la question par 'oui' ou 'non': \n")
