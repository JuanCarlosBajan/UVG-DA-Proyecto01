import timeit
import matplotlib.pyplot as plt

def edit_distance(string1, string2):
		m, n = len(string1), len(string2)
		if m == 0 or n == 0:
				return max(m, n)	# Si alguna de las dos cadenas está vacía, la distancia es la longitud de la otra cadena
		
		if string1[-1] == string2[-1]:
				return edit_distance(string1[:-1], string2[:-1])
		else:
				return 1 + min(edit_distance(string1[:-1], string2), edit_distance(string1, string2[:-1]), edit_distance(string1[:-1], string2[:-1]))

print(edit_distance("hello", "yellow"))