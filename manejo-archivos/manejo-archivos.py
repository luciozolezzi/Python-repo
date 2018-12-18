from io import open


archivo_texto=open("data.txt","w")  #Modo escritura - si no existe, lo crea
#Con "a" lo abro en modo APPEND - agrega informacion al final del archivo_texto

msj="Prueba inscersion de datos\nSegunda linea \n"

archivo_texto.write(msj)    #Escribe en el archivo el mensaje determinado

#Podemos usar el metodo writelines(lista) para escribir una lista de strings en el archivo

archivo_texto.close()   #Cierro la referencia al archivo en memoria
