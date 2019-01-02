#Ejemplos de REGEX (REgular EXPression)

import re

cadena="Cadena de ejemplo para la práctica con expresiones regulares en Python 02/01/2019."
cadena+="En Python es sencillo hacer busquedas con expresiones regulares."
cadena+="21.10.12 19-11-2014 18|11|11."
lista_nombres=['Ana Gonzalez', 'Rodrigo Quispe','Gonzalo Bertinat','Pablo Ocampo',
                'Juan Gonzalez', 'Rodrigo Andreani','Juan Ojeda','Jose Maria Pico',
                'Jose Mario Bertinat']

print(cadena)
objRe=re.search("expresiones",cadena)
print(objRe)    #Busqueda con match
print("Span:",objRe.start(),",",objRe.end())
print(objRe.span())
#objRe.start() devuelve el inicio del span del match
#objRe.end() devuelve el fin del span del match
#objRe.span() devuelve la tupla del match

objRe=re.search("asdasdasda",cadena)
print(objRe)    #Busqueda sin match

#Devuelve un objeto con el span y el match si encontro lo buscado en la Cadena
#Devuelve None si no hay match

matchMutiple=re.findall("Python",cadena)
print(matchMutiple)

#re.findall(busqueda,cadena) encuentra todos los matches de busqueda en la cadena

# METACARACTERES

 #El metacaracter ^ busca todos los que comienzan con Rodrigo
for nombre in  lista_nombres:
    if(re.findall('^Rodrigo',nombre)):
        print('^Rodrigo: '+nombre)


#El metacaracter $ busca todos los que terminan con Gonzalez
for nombre in  lista_nombres:
    if(re.findall('Gonzalez$',nombre)):
        print('Gonzalez$: '+nombre)
#Con [OQJ] busca los nombres que contengan los caracteres O,Q y J, sin importar el orden
for nombre in  lista_nombres:
    if(re.findall('[OQJ]',nombre)):
        print('[OQJ]: '+nombre)

#Busca tanto Mario como Maria
for nombre in  lista_nombres:
    if(re.findall('Mari[oa]',nombre)):
        print('Mari[oa]: '+nombre)

#Ejemplo para buscar fechas
objRe=re.findall('\d\d[-/.\|]{1}\d\d[-/.\|]{1}[0-9][0-9]',cadena)
objRe+=re.findall('\d\d[-/.\|]{1}\d\d[-/.\|]{1}[0-2][0-9][0-9][0-9]',cadena)
print(objRe)
