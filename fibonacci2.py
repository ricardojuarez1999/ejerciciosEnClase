def fibonacci(n):
	numero = [1,1]
	if n == 1:
		return 1
	else:
		for i in range(n+1):
			numero.append(numero[i]+numero[i+1])
		return numero[n]