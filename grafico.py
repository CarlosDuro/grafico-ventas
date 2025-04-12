import pandas as pd
import matplotlib.pyplot as plt

# Cambia esta ruta al lugar donde tienes tu archivo
archivo = r"C:\Users\Carlosd\Ventas.xlsx"

# Leer el archivo Excel
df = pd.read_excel(archivo)

# Ver las columnas para asegurarnos de sus nombres
print(df.columns)

# Crear gráfico de barras
df.groupby('Categoria')['Ventas'].sum().plot(kind='bar')

# Mostrar el gráfico
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas Totales')
plt.show()