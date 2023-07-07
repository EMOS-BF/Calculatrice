def addition(a,b):
    a = float(a)
    b = float(b)
    return a+b

def soustraction(a,b):
    a = float(a)
    b = float(b)
    return a-b

def multiplication(a,b):
    a = float(a)
    b = float(b)
    return a*b

def division(a,b):
    a = float(a)
    b = float(b)
    if b != 0:
        return a/b
    else:
        return 0
    
def power(a,n):
    a = float(a)
    n = float(n)
    return pow(a,n)
