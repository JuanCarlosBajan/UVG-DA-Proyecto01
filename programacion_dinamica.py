import timeit
import matplotlib.pyplot as plt

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)

    # Inicializar una matriz de tamaño (m+1) x (n+1) con ceros
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Llenar la primera fila y la primera columna de la matriz
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Llenar el resto de la matriz
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    # Devolver el valor en la esquina inferior derecha de la matriz
    return dp[m][n]

contenido = []
with open("listado_entradas.txt", "r") as archivo:
    contenido = archivo.read()
    contenido = contenido.split('\n')

times = []
for line in contenido:
    words = line.split(',')
    t = timeit.timeit(stmt=lambda: edit_distance(words[0], words[1]), number=1000)
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
