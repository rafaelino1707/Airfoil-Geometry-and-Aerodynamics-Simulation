import math
from aerodynamic_parameters.dynamic_pressure import *

def lift_per_span(A, N, Angle_of_Atack):
    alpha = math.radians(Angle_of_Atack)
    L = N*math.sin(alpha) + A*math.cos(alpha)

def lift_coefficient(A, N, Angle_of_Atack, V_inf, rho_inf, chord_length, wing_span):
    L_per_span = lift_per_span(A, N, Angle_of_Atack)

    dynamic_press = dynamic_pressure(rho_inf, V_inf)

    return L_per_span / (dynamic_press * chord_length)