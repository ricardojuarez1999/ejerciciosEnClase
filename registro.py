estudiantes={
	
}
r = "si"
r3 = "si"
suma = 0
while r != "no":
	print ("1) crear estudiante")
	print ("2) ingresar notas")
	print ("3) reporte de notas")
	print ("4) salir")
	resp =int(input())
	if  resp == 1:
		est = input("ingrese el nombre del estudiante: ")
		estudiantes[est] = []
	elif resp == 2:
		print ("de que estudiante desea ingresar notas?")
		print (estudiantes)
		resp1 = input("")
		while r3 != "no":
			n = input("ingrese nota: ")
			f = int(n)
			while f < 0 or f >101:
				print ("error, la nota no esta en los parametros")
				n = input("ingrese nota: ")
				f = int(n)
			estudiantes[resp1] += [n]
			print ("desea ingresar otra nota?")
			r3 = (input(""))
	elif resp == 3:
		print ("de que estudiante desea ver las notas?")
		resp2 = input("")
		print (estudiantes[resp2])
		for i in estudiantes[resp2]:
			suma += int(i)
		promedio = suma/len(estudiantes[resp2])
		print ("promedio: ",promedio)
	elif resp == 4:
		r = "no"