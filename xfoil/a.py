import os
import subprocess
import numpy as np

# NACA 9412 parameters
m = 0.12  # Maximum camber (2% of chord)
p = 0.65   # Position of maximum camber (40% of chord)
t = 0.125  # Maximum thickness (12% of chord)
c = 1.0   # Chord length

# Number of points to generate
n = 400
# Generate x coordinates
x = np.linspace(0, c, n)

# Calculate camber line coordinates
y_c = np.zeros_like(x)
for i in range(len(x)):
    if x[i] <= p * c:
        y_c[i] = (m / p**2) * (2 * p * (x[i] / c) - (x[i] / c)**2)

    else:
        y_c[i] = (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * (x[i] / c) - (x[i] / c)**2)

# Calculate thickness distribution
y_t = (t / 0.2) * (0.2969 * np.sqrt(x / c) - 0.1260 * (x / c) - 0.3516 * (x / c)**2 + 0.2843 * (x / c)**3 - 0.1015 * (x / c)**4)

# Calculate upper and lower surface coordinates
y_u = y_c + y_t
y_l = y_c - y_t

# Combine coordinates [::-1]
# print(x)
# print(x[::-1])
# print(np.concatenate((x[::-1], x)))
# print(np.concatenate((y_u[::-1], y_l)))
airfoil_coordinates = np.column_stack((np.concatenate((x[::-1], x)), np.concatenate((y_u[::-1], y_l))))
print(airfoil_coordinates)
# Save to .dat file
#C:/Users/abdurrahman/Desktop/XFOIL/1.dat
with open('airfoil.dat', 'w') as file:
    for coord in airfoil_coordinates:
        file.write(f"{coord[0]:.10f} {coord[1]:.10f}\n")  # Write x and y coordinates

# print("Airfoil coordinates saved to 'airfoil.dat'.")
# Print the coordinates
# for coord in airfoil_coordinates:
#     print(f"{coord[0]:.10f} {coord[1]:.10f}")
        # %% XFOIL input file writer
#
if os.path.exists("polar_file.txt"):
    os.remove("polar_file.txt")

with open("input_file.in", 'w') as input_file:
    input_file.write("LOAD airfoil.dat\n")
    # input_file.write("NACA 2412" + '\n')
    input_file.write("PANE\n")
    input_file.write("\n\n")
    input_file.write("PPAR\n")
    input_file.write("N 400\n")
    input_file.write("T 1 \n")
    input_file.write("\n\n")
    input_file.write("PANE\n")
    input_file.write("OPER\n")
    input_file.write(f"Visc 1000000\n")
    input_file.write(f"Mach 0.5\n")
    input_file.write("PACC\n")
    input_file.write("polar_file.txt\n\n")
    input_file.write("ITER 100\n")
    input_file.write(f"Alfa 5 \n")
    input_file.write("\n\n")
    input_file.write("quit\n")

subprocess.call("xfoil/xfoil.exe < input_file.in", shell=True)



