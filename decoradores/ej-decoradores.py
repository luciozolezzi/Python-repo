"""
    Estructura de los decoradores

def funcion_decorador(funcion):
    def funcion_interna():
        #codigo para decorar
    return funcion_interna

"""

def print_bonito(f_param):
    def funcion_decorada(*args,**kwargs):
        # *args se encarga de los parametros de la funcion a decorar
        print("<*****>")
        f_param(*args,**kwargs)
        print("<*****>")
    return funcion_decorada

@print_bonito
def mensaje():
    print("Mensaje")

@print_bonito
def suma(num1,num2):
    print(num1+num2)

mensaje()   #El mensaje sera imprimido con <*****> arriba y abajo
suma(3,8)   #Prueba con *args
suma(num1=3,num2=8) #prueba con **kwargs
