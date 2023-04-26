import timeit
import matplotlib.pyplot as plt

def edit_distance(string1, string2):
		m, n = len(string1), len(string2)
		if m == 0 or n == 0:
				return max(m, n)	# Si alguna de las dos cadenas está vacía, la distancia es la longitud de la otra cadena
		
		# Divide
		if string1[-1] == string2[-1]:
				return edit_distance(string1[:-1], string2[:-1])
		else:
				return 1 + min(edit_distance(string1[:-1], string2), edit_distance(string1, string2[:-1]), edit_distance(string1[:-1], string2[:-1]))


contenido = []


with open("listado_entradas.txt", "r") as archivo:
    contenido = archivo.read()
    contenido = contenido.split('\n')

times = []
for line in contenido:
    words = line.split(',')
    t = timeit.timeit(stmt=lambda: edit_distance(words[0], words[1]), number=1)
    times.append(t)

etiquetas = list(range(len(times)))

# Crear un gráfico de barras
plt.bar(etiquetas, times)

# Configurar los límites del eje y
plt.ylim([0, max(times) * 1.1])

# Agregar etiquetas de texto para los valores de las barras
for i, valor in enumerate(times):
    plt.text(i, valor * 1.05, str(valor), ha='center')

# Mostrar el gráfico
plt.show()
