from io import open

archivo_texto=open("data.txt","r")  #Abro el archivo en modo lectura
#Para abrir un archivo como R y W, usamos "r+"

texto_lineas=archivo_texto.readlines() #Leo el contenido y genero una lista por lineas del archivo_texto

#Despues de hacer una primera lectura el cursor del archivo queda al final,
#Por lo tanto debemos hacer seek para reposicionar el puntero de la reposicionar

archivo_texto.seek(0)   #Devuelvo el puntero del archivo al comienzo del mismo

#el metodo seek se desplaza por caracteres, no por lineas

texto=archivo_texto.read()  #Leo el contenido del archivo_texto

#Si le pasamos argumento a read(x) lee el archivo hasta el caracter x (y deja el puntero desplazado x caracteres)

archivo_texto.close()   #cierro el archivo_texto

print(texto_lineas)

print(texto)
