import pickle   #Libreria añadida a la standard para manejo de data binaria

archivo=open("data","rb")   #Abre el archivo para lectura binaria

lista=pickle.load(archivo)  #El metodo load() carga la informacion decodificada en la variable lsita

print(lista)

#Tambien se pueden serializar objetos (para leer objetos serializados
#hay que importar la clase del objeto,sino el programa no entiende lo
#que esta leyendo)
