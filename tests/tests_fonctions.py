from : fonction.operation import addition

def test_addition():
    # Test d'addition de deux nombres positifs
    assert addition(2, 3) == 5

    # Test d'addition de deux nombres négatifs
    assert addition(-5, -3) == -8

    # Test d'addition d'un nombre positif et d'un nombre négatif
    assert addition(10, -7) == 3

    print("Tous les tests d'addition ont réussi.")



def test_soustraction():
    # Test de soustraction de deux nombres positifs
    assert soustraction(5, 2) == 3

    # Test de soustraction de deux nombres négatifs
    assert soustraction(-5, -3) == -2

    # Test de soustraction d'un nombre positif et d'un nombre négatif
    assert soustraction(10, -7) == 17

    print("Tous les tests de soustraction ont réussi.")
    
    
    
def test_multiplication():
    # Test de multiplication de deux nombres positifs
    assert multiplication(2, 3) == 6

    # Test de multiplication d'un nombre positif avec zéro
    assert multiplication(4, 0) == 0

    # Test de multiplication de deux nombres négatifs
    assert multiplication(-2, -5) == 10

    # Test de multiplication d'un nombre positif avec un nombre négatif
    assert multiplication(3, -4) == -12
    
    
    
def test_division():
    # Test de division de deux nombres positifs
    assert division(10, 2) == 5

    # Test de division d'un nombre positif par zéro
    if division(8, 0) == "a":
        print("La division par zéro n'a pas été gérée.")
    else:
        print("La division par zéro a été correctement gérée.")

    # Test de division d'un nombre négatif par un nombre positif
    assert division(-15, 3) == -5

    # Test de division d'un nombre positif par un nombre négatif
    assert division(9, -3) == -3

    print("Tous les tests de division ont réussi.")

test_addition()
test_soustraction()
test_soustraction()
test_division()
