"""
Librerias para GUI
    Tkinter ( Es un puente entre Python y la libreria TCL/TK de otros lenguajes)
        $sudo apt-get install pyhton3-tk
    WxPython
    PyQT
    PyGTK
"""
from tkinter import *

#Raiz

raiz=Tk()   #Genero el objeto del tipo Tk para hacer la ventana
raiz.title("GUI-Python")    #Seteo el titulo
raiz.resizable(1,1)     #Habilito el redimensionamiento (Ancho,Alto) (0=false;1=true)
#raiz.iconbitmap("ventana_principal.ico")
raiz.geometry("800x600")    #Seteo la resolucion de la ventana
raiz.config(bg="green")     #Seteo el color del fondo a verde
raiz.config(bd=20,relief="groove")  #Seteo el tipo de borde
raiz.config(cursor="hand2")   #Seteo el comportamiento del cursor en el frame

#Frame

frame1=Frame()
frame1.pack(side="top",pady="50")
frame1.config(bg="blue")    #Seteo el color de fondo del frame
frame1.config(width="600",height="400") #Seteo el tamaño del frame
frame1.config(bd=10,relief="sunken")  #Seteo el tipo de borde
frame1.config(cursor="pirate")   #Seteo el comportamiento del cursor en el frame

#Widgets#
#Label

Label(frame1,text="Label de prueba",fg="white",font=("Comic Sans MS",22),bg="red",bd=10,relief="sunken").place(x="175",y="50")




raiz.mainloop() #Inicio el loop principal de la ventana creada
