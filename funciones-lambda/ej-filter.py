"""
La funcion filter es una funcion de orden superior para paradigma de programacion
funcional. Verifica que los elementos de una secuencia cumplen con una condicion
y devuelve un iterador con los elementos que cumplen dicha condicion

Estructura

objeto_iterable = filter (funcion_a_verificar,lista_de_entradas)

"""

lista_numeros=range(-20,20)

#En este ejemplo imprime los numeros pares y mayores a 0

resultado = list(filter(lambda x: (x%2==0 and x>0),lista_numeros))

print(resultado)
