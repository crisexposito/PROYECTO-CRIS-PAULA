from tkinter import*
import random

def probar(r):
    intento = valor.get()
    if intento>r:
       valor2.set("¡Prueba con un número más pequeño!:)")
                  
    if intento<r:
        valor2.set("¡Prueba con un número más grande!:)")



    if intento == r:
        missatge = "Enhorabuena!"
        valor2.set(missatge)
        mensaje = "Número de intentos= " + str(numero_intentos)
        valor3.set(mensaje)
        
    global numero_intentos   
    numero_intentos= numero_intentos+1
    


#CREAR LA PRIMERA FINESTRA DE L'APLICACIÓ

app = Tk ()

#TITOL I MIDA DE LA FINESTRA
app.title ("ADIVINA EL NÚMERO")

app.geometry ('350x300')
app.config( bg= "#74D5E8")

etiketablanc=Label(app, text = "", bg= "#74D5E8")
etiketablanc.pack()

etiketa1=Label(app, text = "Bienvenido a 'ADIVINA EL NÚMERO'", bg= "#74D5E8")
etiketa1.pack()

etiketablanc1=Label(app, bg= "#74D5E8" ,text = "Tienes que adivinar un número de entre 1 y 100,")
etiketablanc1.pack()
etiketa12= Label(app, text= "ambos incluidos. ¡Adelante!", bg= "#74D5E8")
etiketa12.pack()

r = random.randrange(1,51)

numero_intentos=1
numero_intentos1=1


etiketablanc5=Label(app, text = "", bg= "#74D5E8")
etiketablanc5.pack()

etiketa2= Label(app, text = "Realiza tus intentos...", bg= "#74D5E8")
etiketa2.pack()


etiketablanc6=Label(app, text = "", bg= "#74D5E8")
etiketablanc6.pack()


global valor
valor = IntVar()
caja = Entry(app, textvariable = valor)
caja.pack()

etiketablanc3=Label(app, text = "", bg= "#74D5E8")
etiketablanc3.pack()

boton1 = Button(app, text="Probar", bg="#2F89F5", height= 3, width= 6, command= lambda:probar(r))
boton1.pack()

etiketablanc7=Label(app, text = "", bg= "#74D5E8")
etiketablanc7.pack()


global valor2
valor2=StringVar()
eiketa3 =Label(app, textvariable = valor2, bg= "#74D5E8")
eiketa3.pack()


global valor3
valor3=StringVar()
eiketa89 =Label(app, textvariable = valor3, bg= "#74D5E8")
eiketa89.pack()
