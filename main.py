from fonction.operation import *
from fonction.check import *
from fonction.checkOperation import *
q =1
while q == 1:
    c = 1
    while (c == 1):
        a = input("Entrer un le premier nombre:")
        b = input("Entrer le second nombre:")
        if check(a,b) == 0:
            print("Entrer des nombres entiers SVP")
            c = 1
        else:
            c = 0

    print("Nous avons toutes les operations de base")
    print("Pour addition entrer: +")
    print("Pour la soustration entrer: -")
    print("Pour la multiplication entrer: *")
    print("Pour la division entrer:/")

    k = 1
    while k == 1:
        operation = str(input("Entrer l'operation SVP:"))
        if checkOperation(operation) == 0:
            print("Veuillez Entrez une operation valide")
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
            print("Impossible division par 0")
        else:
            print(division(a,b))
    reponse = input("Voulez vous faire une autre operation\n entrer oui ou non comme reponse:")
    if reponse == "oui":
        q =1
    else:
        q=0