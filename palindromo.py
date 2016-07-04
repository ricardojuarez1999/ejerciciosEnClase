from collections import deque
def palindromo(palabra):
	cola = deque(palabra)
	pila = list(palabra)
	v = 0
	for i in range(len(palabra)):
		if str(cola.popleft()) == str(pila.pop()):
			v += 1
	if v == len(palabra):
		return "es palindromo"
	return "no es palindromo"