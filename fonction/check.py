def check(a,b):
    c = 1
    while (c == 1):
        try:
           int(a) 
           int(b)
           return 1
        except:
            return 0