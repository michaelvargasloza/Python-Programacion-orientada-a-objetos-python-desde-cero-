#Importar algunas funcionalidades de un módulo de la biblioteca estándar
#Nombre a las funciones
from math import sqrt as raiz, pow as exponente

dato = int(input("Ingrese un valor entero: "))
raizcuadrada = raiz(dato)
cubo = exponente(dato, 3)
print("La raíz cuadrada es:", raizcuadrada)
print("El cubo es:", cubo)