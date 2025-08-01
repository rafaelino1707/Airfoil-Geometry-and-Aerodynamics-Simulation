import numpy as np

def y_t(t, x, c, NACA_number):
    x_c = x/c

    char = 0
    for number in NACA_number:
        char+=1
    
    # -- NACA Four-Digit Airfoil --
    if char == 4:
        term1 = 5*(t)
        term2 = (0.2969*np.sqrt(x_c) - 0.1260*x_c - 0.3516*((x_c)**2)
        + 0.2843*((x_c)**3) - 0.1015*((x_c)**4))
        y_t = term1 * term2
        return y_t 
    
'''
- t correspond to the maximum 
thickness of the airfoil expressed as
 a fraction of the chord length
- x is the position along the chord.
- NACA-number corresponde to the
name of the airfoil (i.e. NACA 2241)

'''