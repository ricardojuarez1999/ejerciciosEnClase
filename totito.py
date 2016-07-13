a = 10
tablero = [[65,66,67],[68,69,70],[71,72,73]]
fichas = [[0,0,0],[0,0,0],[0,0,0]]
letras = []
while a !=20:
	sumas = []
	s2 = 0
	s4 = 0
	s5 = 0
	print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
	print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
	print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
	x0 = ord(input("jugador 1, ingrese X: "))
	x = x0 - 65
	fila = x % 3
	columna  = x //3
	if x0 in letras:
		print ("esa casilla esta siendo usada, deseperdicio un turno.")
	else:
		letras.append(x0)
		tablero[columna][fila] = 88
		fichas[columna][fila] = 1
	print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
	print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
	print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
	o0 = ord(input("jugador 2, ingrese O: "))
	o = o0 - 65
	fila = o % 3
	columna  = o //3
	if o0 in letras:
		print ("esa casilla esta siendo usada, desperdicio un turno.")
	else:
		letras.append(o0)
		tablero[columna][fila] = 79
		fichas[columna][fila] = -1
	for i in range(3):
		s = sum(fichas[i])
		sumas.append(s)
		s1 = (fichas[0][i] + fichas[1][i] + fichas[2][i])
		sumas.append(s1)
	print (sumas)