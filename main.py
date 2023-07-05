from fonction.operation import *
from fonction.check import *
from fonction.checkOperation import *
q =1
while q == 1:
    c = 1
    while (c == 1):
        a = input("Entrer un le premier nombre: ")
        print("")
        b = input("Entrer le second nombre: ")
        print("")
        if check(a,b) == 0:
            print("Entrer des nombres entiers SVP")
            c = 1
        else:
            c = 0

    print("Nous avons toutes les operations de base\n")
    print("Pour addition entrer: + \n")
    print("Pour la soustration entrer: -\n")
    print("Pour la multiplication entrer: *\n")
    print("Pour la division entrer: / \n")

    k = 1
    while k == 1:
        operation = str(input("Entrer l'operation SVP: "))
        if checkOperation(operation) == 0:
            print("Veuillez Entrez une operation valide\n")
            k = 1
        else :
            k = 0

    if operation == "+":
        print(addition(a,b))
    elif operation == "-":
        print(soustration(a,b))
    elif operation == "*":
        print(multiplication(a,b))
    elif operation == "/":
        if division(a,b) == "a":
            print("Impossible division par 0\n")
        else:
            print(division(a,b))
    reponse = input("Voulez vous faire une autre operation\n entrer oui ou non comme reponse: \n")
    if reponse == "oui":
        q =1
    else:
        q=0