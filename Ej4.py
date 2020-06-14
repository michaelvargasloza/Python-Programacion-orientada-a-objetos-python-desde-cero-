#Aplicaciones propias con varios módulos
from mayormenor import numero_menor, numero_mayor

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
print("El mayor de los dos es:", numero_mayor(n1, n2))
print("El menor de los dos es:", numero_menor(n1, n2))