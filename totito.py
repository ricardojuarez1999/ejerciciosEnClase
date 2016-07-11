tablero = {
	'fila1' : [65,66,67],
	'fila2' : [68,69,70],
	'fila3' : [71,72,73]
}
a = 10
while a !=20:
	print (chr(tablero['fila1'][0]), chr(tablero['fila1'][1]), chr(tablero['fila1'][2]))
	print (chr(tablero['fila2'][0]), chr(tablero['fila2'][1]), chr(tablero['fila2'][2]))
	print (chr(tablero['fila3'][0]), chr(tablero['fila3'][1]), chr(tablero['fila3'][2]))
	x = input("jugador 1 ingrese X: ")
	if ord(x) == 65 or ord(x) == 97:
		(tablero['fila1'][0]) = 88
	if ord(x) == 66 or ord(x) == 98:
		(tablero['fila1'][1]) = 88
	if ord(x) == 67 or ord(x) == 99:
		(tablero['fila1'][2]) = 88
	if ord(x) == 68 or ord(x) == 100:
		(tablero['fila2'][0]) = 88
	if ord(x) == 69 or ord(x) == 101:
		(tablero['fila2'][1]) = 88
	if ord(x) == 70 or ord(x) == 102:
		(tablero['fila2'][2]) = 88
	if ord(x) == 71 or ord(x) == 103:
		(tablero['fila3'][0]) = 88
	if ord(x) == 72 or ord(x) == 104:
		(tablero['fila3'][1]) = 88
	if ord(x) == 73 or ord(x) == 105:
		(tablero['fila3'][2]) = 88	
	print (chr(tablero['fila1'][0]), chr(tablero['fila1'][1]), chr(tablero['fila1'][2]))
	print (chr(tablero['fila2'][0]), chr(tablero['fila2'][1]), chr(tablero['fila2'][2]))
	print (chr(tablero['fila3'][0]), chr(tablero['fila3'][1]), chr(tablero['fila3'][2]))
	o = input("jugador 2 ingrese O: ")
	if ord(o) == 65 or ord(o) == 97:
		(tablero['fila1'][0]) = 79
	if ord(o) == 66 or ord(o) == 98:
		(tablero['fila1'][1]) = 79
	if ord(o) == 67 or ord(o) == 99:
		(tablero['fila1'][2]) = 79
	if ord(o) == 68 or ord(o) == 100:
		(tablero['fila2'][0]) = 79
	if ord(o) == 69 or ord(o) == 101:
		(tablero['fila2'][1]) = 79
	if ord(o) == 70 or ord(o) == 102:
		(tablero['fila2'][2]) = 79
	if ord(o) == 71 or ord(o) == 103:
		(tablero['fila3'][0]) = 79
	if ord(o) == 72 or ord(o) == 104:
		(tablero['fila3'][1]) = 79
	if ord(o) == 73 or ord(o) == 105:
		(tablero['fila3'][2]) = 79	