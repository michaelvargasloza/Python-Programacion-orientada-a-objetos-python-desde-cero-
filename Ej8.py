#Llamada de métodos desde otro método de la misma clase
class Operacion:
	def __init__(self):
		self.valor1 = 0
		self.valor2 = 0

	def sumar(self):
		suma = self.valor1 + self.valor2
		print("La suma es:", suma)

	def restar(self):
		resta = self.valor1 - self.valor2
		print("La resta es:", resta)

	def multiplicar(self):
		multi = self.valor1 * self.valor2
		print("El producto es:", multi)

	def dividir(self):
		divi = self.valor1 / self.valor2
		print("La división es:", divi)

	def intro_valores(self):
		self.valor1 = int(input("Ingrese primer valor: "))
		self.valor2 = int(input("Ingrese segundo valor valor: "))

	def main(self):
		self.sumar()
		self.restar()
		self.multiplicar()
		self.dividir()

operacion1 = Operacion()
operacion1.intro_valores()
operacion1.main()