
def order_by_strings(strings):
    # strings is a list, order them by the sum of the length of the strings on the array
		# return the ordered list
		return sorted(strings, key=lambda x: sum([len(i) for i in x]))


with open('listado_entradas.txt', 'r'):
		strings = [line.strip().split(',') for line in open('listado_entradas.txt', 'r')]
		ordered = order_by_strings(strings)
		for s in ordered:
			print(s[0] + ',' + s[1])