import pandas as pd
import matplotlib.pyplot as plt

# CAMBIA ESTA LÍNEA con la ruta a tu archivo
EXCEL_PATH = "vllm_metrics.xlsx"

# Leer datos
df = pd.read_excel(EXCEL_PATH)
print(f"Datos cargados: {len(df)} filas")

# Crear figura
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eje izquierdo: requests (AZUL waiting, ROJO running)
line1 = ax1.plot(df['t_rel'], df['num_reqs_waiting'], 'b-o', markersize=4, linewidth=2)
line2 = ax1.plot(df['t_rel'], df['num_reqs_running'], 'r-o', markersize=4, linewidth=2)
ax1.set_xlabel('Tiempo relativo (s)')
ax1.set_ylabel('Número de requests', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True, alpha=0.3)

# CORREGIDO: Primero ax2, luego plot
ax2 = ax1.twinx()
line3 = ax2.plot(df['t_rel'], df['kv_cache_perc'], 'g-o', markersize=4, linewidth=2)
ax2.set_ylabel('KV Cache %', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.set_ylim(0, 0.015)

# Título
plt.title('num reqs wait vs num reqs run vs kv cache usage')

# Leyenda EXACTA (waiting=azul, running=rojo, kv=verde)
lines = line1 + line2 + line3
labels = ['num reqs wait', 'num reqs run', 'kv cache usage']
fig.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.08), 
           ncol=3, fontsize=10, frameon=False)

# Guardar
plt.tight_layout()
plt.savefig('vllm_grafico.png', dpi=300, bbox_inches='tight')
plt.show()

print("¡Gráfico perfecto guardado como 'vllm_grafico.png'!")
