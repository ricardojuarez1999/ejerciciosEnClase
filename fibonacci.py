def fibonacci(n):
	if n == 0:
		return 1
	return fibonacci(n-2)*fibonacci(n-1)