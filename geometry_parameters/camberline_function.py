def y_c(x, m, p, c, NACA_number):
    x_c = x/c

    char = 0
    for number in NACA_number:
        char += 1
    
    print(f'x:{x} p:{p}')
    if char == 4:
        if 0 <= x and x <= p*c:
            y_c = (m/(p**2))*(2*p*x_c-x_c**2)
        if p*c <= x and x <= c:
            y_c = (m/((1-p)**2)) * (1-2*p + 2*p*x_c - x_c**2)
    return y_c

'''
- x is the position along the chord length.
- m is the maximum camber as a fraction of the chord length.
- p is the chordwise position of the maximum camber as a 
fraction of the chord length.

'''