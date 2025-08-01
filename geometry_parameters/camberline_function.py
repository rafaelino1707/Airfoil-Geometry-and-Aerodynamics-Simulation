

def y_c(x, m, p, NACA_number):
    char = 0
    for number in NACA_number:
        char += 1
    
    if char == 4:
        if 0 <= x and x <= p:
            y_c = (m/(p**2))*(2*p*x-x**2)
        if p <= x and x <= 1:
            y_c = (m/((1-p)**2)) * (1-2*p + 2*p*x - x**2)
    
    return y_c

'''
- x is the position along the chord length.
- m is the maximum camber as a fraction of the chord length.
- p is the chordwise position of the maximum camber as a 
fraction of the chord length.

'''