#Redefinición de los operadores matemáticos con objetos
class Operadores:
	def __init__(self, lista):
		self.lista = lista

	def visualizar(self):
		print(self.lista)

	def __add__(self, entero):
		nueva = []
		for x in range(len(self.lista)):
			nueva.append(self.lista[x] + entero)
		return nueva

	def __sub__(self, entero):
		nueva = []
		for x in range(len(self.lista)):
			nueva.append(self.lista[x] - entero)
		return nueva

	def __mul__(self, entero):
		nueva = []
		for x in range(len(self.lista)):
			nueva.append(self.lista[x] * entero)
		return nueva

	def __floordiv__(self, entero):
		nueva = []
		for x in range(len(self.lista)):
			nueva.append(self.lista[x] / entero)
		return nueva

datos = Operadores([19, 23, 58])
datos.visualizar()
print(datos + 2)
print(datos - 2)
print(datos * 2)
print(datos // 2)