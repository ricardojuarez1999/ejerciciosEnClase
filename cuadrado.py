from figura import figurageometrica

class cuadrado(figurageometrica):

	def __init__(self,altura,base):
		super().__init__(base.altura)

	def imprimir(self):
		resultado= ""
		for i in range(self.altura):
			resultado += "*" * self.base
		return resultado
	def calcular_area(self):
		return super().calcular_area