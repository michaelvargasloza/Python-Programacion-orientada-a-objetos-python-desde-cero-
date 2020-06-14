#Objeto file
#Hay que estar en el directorio desde el DOS para crear el archivo.
archivo = open("archivo3.txt", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()
lista = ['Línea 1\n', 'Línea 2']

archivo.writelines(lista)
archivo.seek(final_de_archivo)
#Línea 1
print(archivo.readline())
#Línea 2
print(archivo.readline())