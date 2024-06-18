import matplotlib.pyplot as plt
import numpy as np
import textwrap

fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X * 2 * np.pi) * np.cos(Y * 2 * np.pi)

ax.imshow(Z, cmap='viridis', aspect='auto', extent=[0, 1, 0, 1])

binary_code = "01001111 01110100 01100001 01100011 01101001 01101100 01101001 01101111\n" # Otacilio
binary_code += "01010110 01100001 01101101 01101111 01110011 01110011\n" # Vamoss
binary_code += "01110010 01101111 01100100 01110010 01101001 01100111 01101111 01110010 01100101 01111010\n" # rodrigorez
wrapped_code = textwrap.fill(binary_code * 5, width=60)

ax.text(0.5, 0.5, wrapped_code, fontsize=12, color='white', alpha=0.7, ha='center', va='center', family='monospace')

ax.text(0.5, 0.95, 'Arte e Código Aberto', fontsize=24, color='white', ha='center', va='top', weight='bold')
ax.text(0.5, 0.0, 'https://github.com/OtacilioN/capaArteAberta', fontsize=8, color='white', ha='center', va='bottom')


art_element_x = np.linspace(0.2, 0.8, 500)
art_element_y = np.sin(art_element_x * 13) * 0.1 + 0.5
ax.plot(art_element_x, art_element_y, color='white', lw=2)

ax.axis('off')

plt.show()
