from bs4 import BeautifulSoup
import urllib3

def get_value(data_source):
    l=[]
    for entry in data_source:
        e=str(entry.text).replace(" ","")
        e=e.replace("\n","")
        e=e.replace("\r","")
        e=e.split("$")
        for item in e:
            if(item is not ""):
                l.append(item)
    return l

if __name__ == "__main__":

    url_galicia="https://www.infodolar.com/cotizacion-dolar-entidad-banco-galicia.aspx" 
    #No anda muy bien la pagina, se cae mucho

    http = urllib3.PoolManager()    
    #Pool manager maneja todos los detalles del pooling de la conexion y seguridad de threads

    response = http.request('GET',url_galicia)

    soup = BeautifulSoup(response.data,features="html.parser")

    #print(soup.prettify())

    compra_venta=soup.find_all("td",class_="colCompraVenta")    #findAll es de bs3 y esta deprecado
    variacion=soup.find_all("td",class_="colVariacion")
    spread=soup.find_all("td",class_="colSpread")
    fecha=soup.find_all("td",class_="colFecha")
    nombre_banco=soup.find_all("td",class_="colNombre")

    #Ahora tengo las clases de td que tienen los distintos valores que quiero
    #Lo siguiente es extraer esos valores

    #El resultado de find_all da listas con las ocurrencias,
    #hay que iterar esa lista y sacar los valores

    l_compra_venta=get_value(compra_venta)
    l_variacion=get_value(variacion)
    l_spread=get_value(spread)
    l_fecha=get_value(fecha)
    l_nombre_banco=get_value(nombre_banco)

    print(l_compra_venta)
    print(l_variacion)
    print(l_spread)    
    print(l_fecha)
    print(l_nombre_banco)


