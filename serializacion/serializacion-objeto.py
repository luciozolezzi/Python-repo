import pickle

#Ejemplo de serializacion de clases y guardado permanente

class Persona:

    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona con el nombre de",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):
        lista_personas=open("archivoExterno","ab+")  #"ab" = append binario
        lista_personas.seek(0)

        try:
            self.personas=pickle.load(lista_personas)
            print ("Se cargaron {} personas del archivo externo".format(len(self.personas)))
        except:
            print("El archivo esta vacio")
        finally:
            lista_personas.close()
            del(lista_personas)

    def agregarPersona(self,P):
        self.personas.append(P)
        self.guardarPersonas()

    def listarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        lista_personas=open("archivoExterno","wb")  #"wb"= write binario
        pickle.dump(self.personas,lista_personas)
        lista_personas.close()
        del(lista_personas)

    def mostrarInfoArchivo(self):
        print("La informacion del archivo externo es la siguiente: ")
        for p in self.personas:
            print(p)

mi_lista=ListaPersonas()

"""
p1=Persona("Carlos","M","44")
mi_lista.agregarPersona(p1)
p2=Persona("Mario","M","28")
mi_lista.agregarPersona(p2)
p3=Persona("Carla","F","35")
mi_lista.agregarPersona(p3)
"""

mi_lista.mostrarInfoArchivo()
