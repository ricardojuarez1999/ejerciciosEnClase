def suma(lista):
	if len(lista) == 1:
		return lista[0]
	return lista[0]+suma(lista[1:])