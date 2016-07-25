import ahorcado
palabra = str(ahorcado.palabra_r())
turnos = 0
guiones = []
for i in range(len(palabra)):
	guiones += "_"
while turnos != 7:
	gui = ""
	for i in range(len(palabra)):
		gui += (guiones[i]+" ")
	print (gui)
	print (palabra)
	letra = input("Ingrese una letra: ")
	print (ahorcado.com(palabra,letra))