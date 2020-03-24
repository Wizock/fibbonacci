def fibb(n):
    a = 0
    b = 1

    for i in range(n):
        c = a+b
        a = b
        b = c + a
        print(str(a)+":"+":"+str(c))

fibb(25)
