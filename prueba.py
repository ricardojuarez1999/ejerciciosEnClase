import ahorcado
palabra = (ahorcado.palabra_r())
turnos = 0
guiones = []
ganar = 0
for i in range(len(palabra)):
	guiones += "_"
print ("Bienvenido a ahorcado: \n \n     las reglas son simples \n     si usted falla 7 veces perdera \n     que comience el juego... \n")
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
			ganar +=1
		else:
			letras2 += 1
	if letras2 == len(guiones):
		turnos += 1
		print (ahorcado.suicida(turnos-1))
	if ganar == len(palabra):
		print ("\nusted ha ganado")
		turnos = 7
print ("la palabra correcta era", palabra)