import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
V_DS = [0.15, 1, 1.5, 2, 4, 6, 8, 10, 14.8]  # Voltajes en V
I_D = [0.210, 1.61, 2.43, 3.2, 5.36, 6.48, 7.34, 8, 9.56]  # Corrientes en mA

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(V_DS, I_D, 'bo-', linewidth=2, markersize=8, label='Datos experimentales')

# Personalizar el gráfico
plt.xlabel('$V_{DS}$ [V]', fontsize=12)
plt.ylabel('$I_D$ [mA]', fontsize=12)
plt.title('Característica $I_D$ vs $V_{DS}$ del JFET MPF102', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Añadir anotaciones para algunos puntos importantes
plt.annotate(f'$I_{{DSS}}$ ≈ {I_D[-1]} mA', 
             xy=(V_DS[-1], I_D[-1]), 
             xytext=(V_DS[-1]-2, I_D[-1]+0.5),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, color='red')

# Ajustar los límites del gráfico
plt.xlim(0, 16)
plt.ylim(0, 11)

# Guardar el gráfico
plt.tight_layout()
plt.savefig('./imagenes/grafica_id_vs_vds.png', dpi=300, bbox_inches='tight')
plt.show()