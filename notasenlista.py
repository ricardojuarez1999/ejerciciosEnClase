lista = []
resp = "si"
i=0
while resp != "no":
	nota = int(input("ingrese nota: "))
	lista.append(nota)
	resp = input("desea continuar escribiendo notas? ")
listado = open("notasguardadas.txt", 'w')
for nota in lista:
	i = i+1
	listado.write(str(nota)+"\n")
listado.close()