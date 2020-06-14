#Variables de clase
class Cliente():
	suspendidos = []

	def __init__(self, codigo, nombre):
		self.codigo = codigo
		self.nombre = nombre

	def imprimir(self):
		print("Código:", self.codigo)
		print("Nombre:", self.nombre)
		self.esta_suspendido()

	def esta_suspendido(self):
		if self.codigo in Cliente.suspendidos:
			print("Está suspendido.")
		else:
			print("No está suspendido.")
		print("***************************")

	def suspender(self):
		Cliente.suspendidos.append(self.codigo)

cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3, "Diego")
cliente4 = Cliente(4, "Pedro")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)