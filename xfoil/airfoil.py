import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("NACA Airfoil Generator")

# Sliders for user input
t_c = st.sidebar.slider("Thickness-to-Chord Ratio (t/c)", 0.01, 0.5, 0.12, 0.01)
m_c = st.sidebar.slider("Maximum Camber-to-Chord Ratio (m/c)", 0.0, 0.09, 0.04, 0.01)
p_c = st.sidebar.slider("Position of Maximum Camber (p/c)", 0.0, 0.9, 0.4, 0.1)
c = st.sidebar.slider("Chord Length (c)", 0.1, 10.0, 1.0, 0.1)
n_points = st.sidebar.slider("Number of Points", 100, 400, 400, 10)
re = st.sidebar.slider("Reynold Number", 100000, 3000000, 500000, 10000)
mach = st.sidebar.slider("Mach Number (c)", 0.1, 0.7, 0.5, 0.01)
alfa = st.sidebar.slider("Angel of attack", -5.0, 5.0, 1.0, 0.1)
# print(type(t_c))
# print(float(m_c)*100)
# Generate x coordinates
x = np.linspace(0, c, n_points)

# Calculate normalized thickness distribution
y_t = (5 * t_c) * (0.2969 * np.sqrt(x/c) - 0.1260 * (x/c) -
                   0.3516 * (x/c)**2 + 0.2843 * (x/c)**3 -
                   0.1015 * (x/c)**4)

# Calculate camber line coordinates and slope
y_camber = np.zeros_like(x)
if p_c != 0:
    for i in range(len(x)):
        if x[i] <= p_c * c:
            y_camber[i] = (m_c / (p_c**2)) * (2 * p_c * (x[i]/c) - (x[i]/c)**2)
        else:
            y_camber[i] = (m_c / ((1-p_c)**2)) * ((1-2*p_c) + 2*p_c*(x[i]/c) - (x[i]/c)**2)


y_upper = y_camber + y_t
y_lower = y_camber - y_t

# Plotting the airfoil
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x*c, y_upper*c, label='Upper Surface', color='blue')
ax.plot(x*c, y_lower*c, label='Lower Surface', color='red')
ax.plot(x*c, y_camber*c, label='Camber Line', color='green')
ax.axhline(0, color='black', lw=0.5, ls='--')  # x-axis
ax.axvline(0, color='black', lw=0.5, ls='--')  # y-axis
ax.set_title(f'NACA {int(m_c*100)}{int(p_c*10)}{int(t_c*100)} Airfoil')
ax.set_xlabel('Chord Position (x)')
ax.set_ylabel('Thickness (y)')
ax.set_xlim(0, c)
ax.set_ylim(-0.1, 0.1)  # Adjust y-limits for better visibility
ax.grid()
ax.legend()
ax.axis('equal')  # Equal aspect ratio

# Show the plot in Streamlit
st.pyplot(fig)




st.write("Airfoil Data:")

airfoil_coordinates = np.column_stack((np.concatenate((x[::-1], x)), np.concatenate((y_upper[::-1], y_lower))))
# Save to .dat file
with open('airfoil.dat', 'w') as file:
    for coord in airfoil_coordinates:
        file.write(f"{coord[0]:.10f} {coord[1]:.10f}\n")  # Write x and y coordinates

# Create a download button
with open('airfoil.dat', 'rb') as f:
    st.download_button(
        label="Download airfoil data",
        data=f,
        file_name='airfoil.dat',
        mime='application/octet-stream'
    )

st.write("Calculate Coefficients (Cl, Cd, Cm)")
if st.button("Calculate"):

    if os.path.exists("polar_file.txt"):
        os.remove("polar_file.txt")

    with open("input_file.in", 'w') as input_file:
        input_file.write("LOAD airfoil.dat\n")
        # input_file.write("NACA 2412" + '\n')
        # input_file.write("\n\n")
        # input_file.write("PPAR\n")
        # input_file.write("N 400\n")
        # input_file.write("T 1 \n")
        input_file.write("\n\n")
        input_file.write("PANE\n")
        input_file.write("OPER\n")
        input_file.write(f"Visc {re}\n")
        input_file.write(f"Mach {mach}\n")
        input_file.write("PACC\n")
        input_file.write("polar_file.txt\n\n")
        input_file.write("ITER 100\n")
        input_file.write(f"Alfa {alfa} \n")
        input_file.write("\n\n")
        input_file.write("quit\n")

    subprocess.call("xfoil.exe < input_file.in", shell=True)

    # Initialize variables to store the extracted values
    CL = CD = CDp = CM = None

    # Open the file and read its contents
    with open('polar_file.txt', 'r') as file:
        for line in file:
            # Check if the line contains the polar data
            if '------' in line:
                # Read the next line which contains the values
                next_line = next(file)

                # Split the line into individual components
                values = next_line.split()
                # Extract the values for CL, CD, CDp, and CM
                alpha = float(values[0])  # Alpha (angle of attack)
                CL = float(values[1])      # Lift Coefficient
                CD = float(values[2])      # Drag Coefficient
                CDp = float(values[3])     # Profile Drag Coefficient
                CM = float(values[4])      # Moment Coefficient
                break  # Exit the loop after finding the values

    st.write(f"Lift Coefficient:   {CL}")
    st.write(f"Drag Coefficient:   {CD}")
    st.write(f"Moment Coefficient: {CM}")
    st.write(f"Lift to Drag Ratio: {CL/CD}")
    # Print the extracted values
    # print(f"\n\n\nCL: {CL}, CD: {CD}, CDp: {CDp}, CM: {CM}")
    # print(f"\n CL/CD: {CL/CD}")

