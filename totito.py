ganador = False
tablero = [[65,66,67],[68,69,70],[71,72,73]]
fichas = [[0,0,0],[0,0,0],[0,0,0]]
letras = []
print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
while ganador == False :
	seriedad = False
	sumas = []
	d1 = 0
	d2 = 0
	while seriedad != True:
		x0 = ord(input("jugador 1, ingrese X: "))
		if x0 <= 64 or x0 >= 74:
			print ("jugador 1, ese caracter no es valido, sea serio por favor.")
		else:
			x = x0 - 65
			fila = x % 3
			columna  = x // 3
			if x0 in letras:
				print ("esa casilla esta siendo usada, jugardor 1 sea serio, por favor hagalo de nuevo.")
			else:
				letras.append(x0)
				tablero[columna][fila] = 88
				fichas[columna][fila] = 1
				seriedad = True
				for i in range(3):
					horizontal = sum(fichas[i])
					sumas.append(horizontal)
					vertical = (fichas[0][i] + fichas[1][i] + fichas[2][i])
					sumas.append(vertical)
					d1 += fichas[i][i]
					d2 += fichas[i][2-i]
					sumas.append(d1)
					sumas.append(d2)
				if 3 in sumas:
					print ("el jugador 1 ha ganado")
					ganador = True
					juego = True
				else:
					d1 = 0
					d2 = 0
					juego = False
	print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
	print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
	print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
	while juego == False:
		while seriedad != False:
			o0 = ord(input("jugador 2, ingrese O: "))
			if o0 <= 64 or o0 >= 74:
				print ("jugador 2, ese caracter no es valido, sea serio por favor.")
			else:
				o = o0 - 65
				fila = o % 3
				columna  = o //3
				if o0 in letras:
					print ("esa casilla esta siendo usada, jugardor 2 sea serio, por favor hagalo de nuevo.")
				else:
					letras.append(o0)
					tablero[columna][fila] = 79
					fichas[columna][fila] = -1
					seriedad = False
		sumas = []
		for i in range(3):
			horizontal = sum(fichas[i])
			sumas.append(horizontal)
			vertical = (fichas[0][i] + fichas[1][i] + fichas[2][i])
			sumas.append(vertical)
		for i in range(3):
			d1 += (fichas[i][i])
			d2 += (fichas[i][2-i])
		sumas.append(d1)
		sumas.append(d2)
		if -3 in sumas:
			print ("el ganador 2 ha ganado")
			ganador = True
			juego = True
		else:
			juego = True
		print (chr(tablero[0][0]), chr(tablero[0][1]), chr(tablero[0][2]))
		print (chr(tablero[1][0]), chr(tablero[1][1]), chr(tablero[1][2]))
		print (chr(tablero[2][0]), chr(tablero[2][1]), chr(tablero[2][2]))
		print (sumas)