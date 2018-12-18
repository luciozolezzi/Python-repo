import pickle   #Libreria añadida a la standard para manejo de data binaria

lista_nombres = ["Juan","Lucio","Rodri","Pablo","Jose"]

archivo_binaro=open("data","wb")    #Si no se le especifica, el archivo data es binario
                                    #"wb" es escritura binaria
pickle.dump(lista_nombres,archivo_binaro)   #Vuelca en el archivo binario la data en forma binaria

archivo_binaro.close()  #Cierro el archivo con la informacion guardada

del(archivo_binaro) #Con del() borro de memoria el archivo binario
