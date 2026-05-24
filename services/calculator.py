def calc_stuff(a, b, c, f):
    if a != None:
        if b > 0:
            x = a * b
            if f == True:
                y = x - c
                return y
            else:
                return x
    return 0
