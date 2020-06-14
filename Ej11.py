#Herencia
class Operacion:
	def __init__(self):
		self.valor1 = 0
		self.valor2 = 0
		self.resultado = 0

	def cargar(self):
		self.valor1 = int(input("Ingrese primer valor: "))
		self.valor2 = int(input("Ingrese segundo valor: "))

	def mostrar_resultado(self):
		print(self.resultado)

class Suma(Operacion):
	def operar(self):
		self.resultado = self.valor1 + self.valor2

class Resta(Operacion):
	def operar(self):
		self.resultado = self.valor1 - self.valor2

suma1 = Suma()
suma1.cargar()
suma1.operar()
print("La suma de los valores es: ")
suma1.mostrar_resultado()

resta1 = Resta()
resta1.cargar()
resta1.operar()
print("La resta de los valores es: ")
resta1.mostrar_resultado()