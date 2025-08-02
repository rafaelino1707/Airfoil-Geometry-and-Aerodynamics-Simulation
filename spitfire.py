import numpy as np
import matplotlib.pyplot as plt

# Parâmetros típicos de Spitfire Mk IX
b = 11.2  # envergadura total em metros
cr = 2.3  # corda na raiz

# Apenas metade da asa
x = np.linspace(0, b/2, 200)
y = (np.sqrt(1 - (2*-x/b)**2)) * (cr / 2)

# Espelhar para obter o contorno completo
x_full = np.concatenate([x, x[::-1]])
y_full = np.concatenate([y, -y[::-1]])

# Plot
plt.figure(figsize=(10, 2))
plt.plot(x_full, y_full, 'k')
plt.axis('equal')
plt.axis('off')
plt.savefig("spitfire_wing.svg", format="svg")
plt.show()
