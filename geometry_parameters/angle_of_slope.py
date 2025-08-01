import math


def theta(x, m, p, c, NACA_number):
    x_c = x/c

    char = 0
    for number in NACA_number:
        char += 1
    
    if char == 4:
        if 0 <= x and x <= p*c:
            dyc_dx = (m/(p**2))*(2*p-2*x_c)
            theta = math.atan(dyc_dx)
        if p*c <= x and x <= c:
            dyc_dx = (m/((1-p)**2)) * (1-2*p + 2*p - 2*x_c)
            theta = math.atan(dyc_dx)

    return theta # radians

'''
- x is the position along the chord length.
- m is the maximum camber as a fraction of the chord length.
- p is the chordwise position of the maximum camber as a 
fraction of the chord length.

'''