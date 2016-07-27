import ahorcado
palabra = list(ahorcado.palabra_r())
turnos = 0
guiones = []
for i in range(len(palabra)):
	guiones += "_"
while turnos != 7:
	gui = ""
	letras2 = 0
	for i in range(len(palabra)):
		gui += (guiones[i]+" ")
	print (gui)
	letra = input("Ingrese una letra: ")
	for i in range(len(guiones)):
		if letra == palabra[i]:
			guiones[i] = letra
		else:
			letras2 += 1
	if letras2 == len(guiones):
		turnos += 1
		print (ahorcado.suicida(turnos-1))