#Objeto file
#Hay que estar en el directorio desde el DOS para crear el archivo.
archivo = open("archivo2.txt", "w+")
seleccion = input("Introduce el texto para el archivo: ")
contenido = archivo.read()
final_de_archivo = archivo.tell()

archivo.write(seleccion)
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()

archivo.close()

print(nuevo_contenido)