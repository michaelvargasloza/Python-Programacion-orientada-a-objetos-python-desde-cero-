#Método constructor de clase
class Usuario:
	def __init__(self):
		self.usuario = ""
		self.ingresos = 0

	def intro(self):
		self.usuario = input("Ingrese el nombre del usuario: ")
		self.ingresos = float(input("Cantidad ingresos anual: "))

	def visualizar(self):
		print("Nombre:", self.usuario)
		print("Ingresos:", self.ingresos)

	def fiscalidad(self):
		if self.ingresos > 3000:
			print("Debe pagar impuestos.")
		else:
			print("No paga impuestos.")

usuario = Usuario()
usuario.intro()
usuario.visualizar()
usuario.fiscalidad()