#Redefinición de los operadores relacionales con 
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def __eq__(self, objeto2):
		if self.edad == objeto2.edad:
			return True
		else:
			return False

	def __ne__(self, objeto2):
		if self.edad != objeto2.edad:
			return True
		else:
			return False

	def __gt__(self, objeto2):
		if self.edad > objeto2.edad:
			return True
		else:
			return False

	def __ge__(self, objeto2):
		if self.edad >= objeto2.edad:
			return True
		else:
			return False

	def __lt__(self, objeto2):
		if self.edad < objeto2.edad:
			return True
		else:
			return False

	def __le__(self, objeto2):
		if self.edad <= objeto2.edad:
			return True
		else:
			return False

persona1 = Persona("Juan", 22)
persona2 = Persona("Ana", 22)
if persona1 == persona2:
	print("Las dos personas tienen la misma edad.")
else:
	print("No tienen la misma edad.")