def maximo(lista):
	if len(lista)==1:
		return lista[0]
	sublista = lista[1:]
	maximolista = maximo(sublista)
	if lista[0] > maximolista :
		return lista[0]
	return maximolista		