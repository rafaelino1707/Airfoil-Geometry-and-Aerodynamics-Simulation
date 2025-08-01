import numpy as np
import matplotlib.pyplot as plt
import math
from geometry_parameters.thickness_distribution import *
from geometry_parameters.camberline_function import *
from geometry_parameters.angle_of_slope import *

# NACA 0018
NACA = "2412"
t = 0.12
c = 1.0
m = 0.02
p = 0.4
n_points = 10000

xs = np.linspace(0, c, n_points)

ys_camber = []
ys_chord = []
xs_upper = []
xs_lower = []
ys_upper = []
ys_lower = []


for x in xs:
    # Thickness Distribution
    yt = y_t(t, x, c, NACA)

    # Camberline Function
    y_camber = y_c(x, m, p, NACA)
    ys_camber.append(y_camber)

    # Calculate chord line coordinates
    y_chord = 0 * x
    ys_chord.append(y_chord)

    # Angle of Slope
    Theta = theta(x, m, p, NACA)

    # Leading edge radius calculation (not used directly in plotting)
    r_t = 1.1019 * ((t/c)**2)

    x_upper = x - yt*math.sin(Theta)
    x_lower = x + yt*math.sin(Theta)
    xs_upper.append(x_upper)
    xs_lower.append(x_lower)

    y_upper = y_camber + yt*math.cos(Theta)
    y_lower = y_camber - yt*math.cos(Theta)
    ys_upper.append(y_upper)
    ys_lower.append(y_lower)

# Plotting the airfoil
plt.figure(figsize=(20, 10))
plt.plot(xs_upper, ys_upper, label='Upper Surface', color='blue')
plt.plot(xs_lower, ys_lower, label='Lower Surface', color='red')
plt.plot(xs, ys_camber, label='Camber Line', color='green')
plt.plot(xs, ys_chord, label='Chord Line', color='black', linestyle='--')
plt.title('NACA 2412 Airfoil')
plt.xlabel('Chord Position (x/c)')
plt.ylabel('Thickness (y/c)')
plt.axhline(0, color='black', lw=2, ls='--')  # x-axis
plt.axvline(0, color='black', lw=2, ls='--')  # y-axis
plt.xlim(0, c)
plt.ylim(-0.1, 0.1)  # Adjust y-limits for better visibility
plt.grid()
plt.legend()
plt.axis('equal')  # Equal aspect ratio
plt.show()

