#Clases y objetos
class Alumno:
	def declarar(self, nombre, dato):
		self.nombre = nombre
		self.puntuacion = dato

	def visualizar(self):
		print("Nombre:", self.nombre)
		print("Puntuación:", self.puntuacion)

	def estadistica(self):
		if self.puntuacion <= 4:
			print("Insuficiente.")
		elif self.puntuacion >= 5:
			print("Notable.")
		elif self.puntuacion >= 8:
			print("Sobresaliente.")
		else:
			print("Libre.")

alumno1 = Alumno()
alumno1.declarar("Diego", 2)
alumno1.visualizar()
alumno1.estadistica()

alumno2 = Alumno()
alumno2.declarar("Ana", 10)
alumno2.visualizar()
alumno2.estadistica()