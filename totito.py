a = 10
tablero = [[65,66,67],[68,69,70],[71,72,73]]
fichas = [[0,0,0],[0,0,0],[0,0,0]]
letras = []
while a !=20:
	print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
	print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
	print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
	x0 = ord(input("ingrese x: "))
	x = x0 - 65
	fila = x % 3
	columna  = x //3
	letras.append(x0)
	if x0 in letras:
		"esa casilla esta siendo usada, pierde un turno."
	else:
		tablero[columna][fila] = 88
	print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
	print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
	print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
	o0 = ord(input("ingrese o: "))
	o = o0 - 65
	fila = o % 3
	columna  = o //3
	letras.append(o0)
	if o0 in letras:
		"esa casilla esta siendo usada, pierde un turno."
	else:
		tablero[columna][fila] = 79