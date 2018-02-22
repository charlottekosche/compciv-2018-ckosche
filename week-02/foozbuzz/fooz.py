def fob (x):
    for i in range (1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print (i, "foozbuzz")
        elif i % 3 == 0:
            print (i, "fooz")
        elif i % 5 == 0:
            print (i, "buzz")
        else: print (i)