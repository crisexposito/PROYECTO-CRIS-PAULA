from tkinter import*
import sqlite3
import random 
import pygame

import time
from pygame.locals import *


#FUNCIONS PRIMERA FINESTRA
def usuarios():
    global db
    db = sqlite3.connect ("CriPaBot")
    global c
    c = db.cursor()
    usuario = cajau.get()
    contraseña = cajap.get()
    
    c.execute('SELECT * FROM usuarios WHERE usuario=? AND contraseña=?', (usuario, contraseña))
    if c.fetchall():
        eleccion()
    else:    
        messagebox.showerror(title="LogIn incorrecto", message = "Usuario y contraseña incorrectos")
        c.close()

def nuevo():
    global db
    db = sqlite3.connect ("CriPaBot")
    global c
    c = db.cursor()
    c.execute('INSERT INTO usuarios (usuario, contraseña) VALUES(?,?)', (valor1.get(), valor2.get()))
    db.commit()
    messagebox.showinfo(title="Felicidades!", message="Ya eres miembro de CriPaBot.")
 
def limpiar():
    global c
    valor1.set("")
    valor2.set("")

#################################
#FUNIONS BOTONS 
def btnClic(n):
    add=v.get()
    
    text=add+str(n)
    v.set(text)

def btnIgual():
    op=v.get()
    resultat = str(eval(op))
    global intronum
    intronum.set(resultat)

def btnAns():
    ans=intronum.get()
    v.set(ans)

def btnClear():
    clearing = str(0)
    intronum.set(clearing)
    v.set("")

    #FUNCIONS MENU
def saludo():
    v.set("BUENOS DÍAS!")

def ayuda():
    v.set("Pulsa teclas y calcula")
        
def clear():
    v.set("")
    intronum.set("0")

    #SORTIDA DEL RESULTAT FINAL + OPERACIÓ QUE S'HA DE FER
def resultatsum():
    sortidasum = str((float(num1.get())) + (float(num2.get())))
    respostasum.set(sortidasum)
        
def resultatres():
    sortidares = str((float(num1.get())) - (float(num2.get())))
    respostares.set(sortidares)
        
def resultatmul():
    sortidamul = str((float(num1.get())) * (float(num2.get())))
    respostamul.set(sortidamul)

def resultatdiv():
    sortidadiv = str((float(num1.get())) / (float(num2.get())))
    respostadiv.set(sortidadiv)
#FINESTRA CALCULADORA
def calcu():
 
    #CREAR LA PRIMERA FINESTRA DE L'APLICACIÓ
    app = Toplevel()

    #CAMBIAR COLOR DE LA FINESTRA
    app.config(bg="blue")

    #TITOL I MIDA DE LA FINESTRA
    app.title ("CALCULADORA")
    app.geometry ('185x250')

    #MENÚ
    #1.barra menu
    barramenu = Menu(app)
    #2.crear menú
    menuArchivo= Menu(barramenu)
    #3.crear archius dins menu
    menuArchivo.add_command(label="Saludar", command=lambda:saludo())
    menuArchivo.add_command(label="Ayuda", command=lambda:ayuda())
    menuArchivo.add_command(label="Limpiar cajas", command=lambda:clear())
    menuArchivo.add_command(label="Cerrar", command=app.destroy)
    #4.afegir els menus a la barra de menus
    barramenu.add_cascade(label="Archivo", menu=menuArchivo)
    #5.indicar que la barra de menus estirà en la finestra
    app.config(menu=barramenu)

    #CAIXA ON SORTIRAN ELS NUMEROS
    global v
    v = StringVar()
    caixa2 = Entry(app, textvariable=v, width=21)
    caixa2.grid(column=1, row=1, columnspan=4)
    global intronum
    intronum = StringVar()
    caixa = Entry(app, textvariable=intronum, width=21)
    caixa.grid(column=1, row=2, columnspan=4)

    #CREAR BOTONS suma resta...
    botonclear = Button(app, text="Clear", height=2, width=3, command = lambda:btnClear(), bg="#0056FF" ,cursor="hand1")
    botonclear.grid(column=1, row=3, columnspan=2)

    botonans = Button(app, text="Ans", height=2, width=3, command = lambda:btnAns(), bg="#0056FF" ,cursor="hand1")
    botonans.grid(column=3, row=3, columnspan=4)

    botons = Button(app, text="+", command=lambda:btnClic("+"), height=2, width=2, bg="#476BB3" ,cursor="hand1")
    botons.grid(column=4, row=4)

    botonr = Button(app, text="-", command=lambda:btnClic("-"), height=2, width=2, bg="#476BB3" ,cursor="hand1")
    botonr.grid(column=4, row=5)

    botonm = Button(app, text="*", command=lambda:btnClic("*"), height=2, width=2, bg="#476BB3", cursor="hand1")
    botonm.grid(column=4, row=6)

    botond = Button(app, text="/",command=lambda:btnClic("/"),  height=2, width=2, bg="#476BB3" ,cursor="hand1")
    botond.grid(column=4, row=7)

    #CREAR BOTONS numeros..
    boton7 = Button(app, text="7",command=lambda:btnClic(7),  height=2, width=2, bg="#6699FF",cursor="hand1")
    boton7.grid(column=1, row=4)

    boton8 = Button(app, text="8", command=lambda:btnClic(8), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton8.grid(column=2, row=4)

    boton9 = Button(app, text="9", command=lambda:btnClic(9), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton9.grid(column=3, row=4)

    boton4 = Button(app, text="4", command=lambda:btnClic(4), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton4.grid(column=1, row=5)

    boton5 = Button(app, text="5", command=lambda:btnClic(5), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton5.grid(column=2, row=5)

    boton6 = Button(app, text="6", command=lambda:btnClic(6), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton6.grid(column=3, row=5)

    boton1 = Button(app, text="1",command=lambda:btnClic(1),  height=2, width=2, bg="#6699FF",cursor="hand1")
    boton1.grid(column=1, row=6)

    boton9 = Button(app, text="2", command=lambda:btnClic(2), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton9.grid(column=2, row=6)

    boton3 = Button(app, text="3", command=lambda:btnClic(3), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton3.grid(column=3, row=6)

    boton9 = Button(app, text="0", command=lambda:btnClic(0), height=2, width=2, bg="#6699FF",cursor="hand1")
    boton9.grid(column=2, row=7)

    botonig = Button(app, text="=", command=lambda:btnIgual(), height=2, width=2, bg="#0056FF",cursor="hand1")
    botonig.grid(column=3, row=7)

    botoncom = Button(app, text=",", command=lambda:btnClic(","), height=2, width=2, bg="#0056FF",cursor="hand1")
    botoncom.grid(column=1, row=7)

    #DARRERA ETIQUETA ON SORTIRÀ EL TEXT ESCRIT DINS LA CAIXA
    respostasum = StringVar()
    etiketa2 = Label (app, textvariable=respostasum)
    etiketa2.grid()
   

#################################
#DEFINIM LA SEGONA FINESTRA
def eleccion():
    messagebox.showinfo(title="LogIn correcto ", message= "Usuario y contraseña correctas. ¡A divertirse!")
    ventana1.destroy()
    global ventana2
    ventana2 = Tk()
    ventana2.title ("CriPaBot")
    ventana2.geometry ('311x300')    
    ventana2.config(bg = "#74D5E8")

#########################
#CRIPABOT
    def cripabot(): 
        print ("Hola! Me llamo CriPaBot, vas a iniciar una conversación conmigo.")
        time.sleep(3)
        print ("Pero como soy muy joven necesito que me hables con respuestas claras y breves.")
        time.sleep(3)
        print ("Todavia necesito aprender.")
        time.sleep(3)

        nombre= input ("¿Como te llamas?")
        time.sleep(2)
        print ("Bonito nombre,", nombre)
        time.sleep(3)

##################################

        edad= int (input ("¿Que edad tienes?"))
        if edad < 30:
            time.sleep(2)
            print("Sigues siendo joven ^^")
            time.sleep(2)
        elif edad >= 30:
            time.sleep(2)
            print("Pues no veo el baston en tu mano")
            time.sleep(2)

        #######################

        bienmal= input ("¿Cómo estas? (bien/mal)")
        if (bienmal) == "bien":
            time.sleep(2)
            print("Esa felicidad no te durará mucho")
            time.sleep(2)
        if (bienmal) == "mal":
            time.sleep(2)
            print("Bueno, con este test te animarás ;)")
            time.sleep(2)  
                
        #######################

        estado= input ("¿Tienes pareja?")
        if (estado) == "si":
            time.sleep(2)
            print("Que gracia tienes")
            time.sleep(2)
        elif (estado) == "no":
            time.sleep(2)
            print("Soltero y entero!!")
            time.sleep(2)

        #######################

        estudias= input ("¿Estudias?")
        if (estudias) == "si":
            time.sleep(2)
            print("De cada vez veo que tienes una vida de lo más aburrida")
            time.sleep(2)
        elif (estudias) == "no":
            time.sleep(2)
            print("Pues estas jodido")
            time.sleep(2)

        #######################

        print ("Se me ha ocurrido un juego!!")
        time.sleep(2)
        print ("Responde con el numero correspondiente a la opción que elijas")
        time.sleep(2)
        print ("He bautizado el juego como: '¿Qué prefieres?'")
        time.sleep(1)

        repetir=True
        while repetir == True:
            respuesta= input("¿Quieres jugar? (s/n)")
            if (respuesta) == "n":
                repetir=False
                print ("Que aburrido.. yo que lo hacia por jugar un rato. Adiós.")
            if (respuesta) == "s":
                repetir = True
                print ("Ahí va mi primera propuesta.")
                time.sleep(1)
                print ("Piénsalo bien antes de contestar eeh")
                time.sleep(2)

                print ("1. ¿Ganar 100.000€ ahora mismo?")
                print ("2. ¿Ganar 1.000.000€ dentro de 10 años?")
                resp1=input ("¿Qué prefieres?(1/2)")
                if resp1 == "1":
                    print ("Que prisas tienes?")
                    time.sleep(2)
                elif resp1 == "2":
                    print ("Te sabes economizar")
                    time.sleep(2)
                print("Segunda propuesta:")
                time.sleep(2)

                print ("1. ¿Pasar 1 año en tu trabajo cobrando el triple?")
                print ("2. ¿Pasar 1 sin currar pero cobrando tu sueldo?")
                resp2=input ("¿Qué prefieres?(1/2)")
                if resp2 == "1":
                    print ("Tantas ganas de currar tienes?")
                    time.sleep(2)
                elif resp2 == "2":
                    print ("Te va la comodidad eh cabrón ;)")
                    time.sleep(2)
                print("Siguiente propuesta:")
                time.sleep(2)
                
                print ("1. ¿Vivir en una prisión?")
                print ("2. ¿Vivir en el país más pobre del mundo?")
                resp3=input ("¿Qué prefieres?(1/2)")
                if resp3 == "1":
                    print("Si yo pudiera vivir, también lo preferiria")
                    time.sleep(2)
                elif resp3 == "2":
                    print ("Que vida más cruel te espera pues..")
                    time.sleep(2)
                print("Continuemos..")
                time.sleep(2)
                 
                print ("1. ¿Tener un chef personal?")
                print ("2. ¿Tener un chofer personal?")
                resp4=input ("¿Qué prefieres?(1/2)")
                if resp4 == "1":
                    print("Mmmm... suena bien")
                    time.sleep(2)
                elif resp4 == "2":
                    print ("Que vago eres")
                    time.sleep(2)
                print("Déjame pensar...")
                time.sleep(2)

                print ("1. ¿Sólo necesitar dormir 5 horas al día?")
                print (" 2. ¿Dormir 10 horas al día pero controlar lo que sueñas?")
                resp5=input ("¿Qué prefieres?(1/2)")
                if resp5 == "1":
                    print ("Buena elección, yo no sabría que elegir")
                    time.sleep(2)
                elif resp5 == "2":
                    print("Curioso..")
                    time.sleep(2)
                print("Prosigamos..")
                time.sleep(2)

                print ("1. ¿Tener mucha más oida, pero quedarte ciego?")
                print ("2. ¿Tener mucha mas vista, pero quedarte sordo?")
                resp6=input ("¿Qué prefieres?(1/2)")
                if resp6 == "1":
                    print("¿Enserio?")
                    time.sleep(2)
                elif resp6 == "2":
                    print ("¿Enserio?")
                    time.sleep(2)
                print("Otra más..")
                time.sleep(2)

                print ("1. ¿Sólo tener ropa de invierno en verano?")
                print ("2. ¿Sólo tener ropa de verano en invierno?")
                resp7=input ("¿Qué prefieres?(1/2)")
                if resp7 == "1":
                    print ("Que calor!")
                    time.sleep(2)
                elif resp7 == "2":
                    print ("Que frío!")
                    time.sleep(2)
                print("Siguiente propuesta:")
                time.sleep(2)

                print ("1. ¿Tener un botón para rebobinar en tu vida?")
                print ("2. ¿Tener un botón para pausar en tu vida?")
                resp8=input ("¿Qué prefieres?(1/2)")
                if resp8 == "1":
                    print ("Con el botón podrías parar el tiempo ;)")
                    time.sleep(2)
                elif resp8 == "2":
                    print ("Yeah")
                    time.sleep(2)
                print("Una difícil")
                time.sleep(2)

                print ("1. ¿Que tu pareja te pille poniéndole los cuernos? ")
                print ("2. ¿Pillar a tu preja poniéndote los cuernos?")
                resp9=input ("¿Qué prefieres?(1/2)")
                if resp9 == "1":
                    print ("Pobrecilla tu pareja..")
                    time.sleep(2)
                elif resp9 == "2":
                    print ("Que valiente")
                    time.sleep(2)
                print("¿Sabrás contestar la siguiente..?")
                time.sleep(2)
                
                print ("1. ¿Acabar con el machismo?")
                print ("2. ¿Acabar con el racismo?")
                resp10=input ("¿Qué prefieres?(1/2)")
                if resp10 == "1":
                    print ("¿Y el racismo qué?")
                    time.sleep(2)
                elif resp10 == "2":
                    print ("¿Y el machismo qué?")
                    time.sleep(3)
                print("Gracias por jugar conmigo! Me tengo que ir, adiós! :)")
                break
        
        print("by: Cris Expósito y Paula Gomila")


################################
    def chistes():
        messagebox.showinfo( title="Publicidad", message="-¿Que hace una abeja en un gimnasio?    -....Zumba")
        messagebox.showinfo( title="Publicidad", message="-¿Sabes que coche usa Papá Noel?  -Fácil... un Renol")
        messagebox.showinfo( title="Publicidad", message="-Tío, ¿Sabes que puedo adivinar el futuro?  -¿Desde cuando? -Desde el jueves que viene!")
        messagebox.showinfo( title="Publicidad", message="-Doctor, quería hacerle una consulta. -Me alegro, esta consulta se me esta quedando pequeña.")
        messagebox.showerror( title="Error", message="La página no se puede cargar. Pruebe más tarde")
                

#################################3
#CAIXES I ETIKETES SEGONA FINESTRA
    etiketaintro = Label (ventana2, text= "Es hora de divertirse!", bg= "#FCF8C0")
    etiketaintro.pack()
    
    etiketaintro2 = Label (ventana2, text= "Elije dónde quieres entrar", bg= "#FCF8C0")
    etiketaintro2.pack()

    etiketabla1 = Label ( ventana2, text= "", bg= "#6B6B6B")
    etiketabla1.pack()
    
    btncripa = Button (ventana2, text= "CriPaBot", command= cripabot, height=3, width=14, bg= "#FCF8C0", cursor="hand1")
    btncripa.pack()
    
    btncal = Button (ventana2, text= "Calculadora", command= calcu, height=3, width=14, bg= "#FCF8C0", cursor="hand1")
    btncal.pack()

    btnentre = Button (ventana2, text= "Entretenimiento", command= juegos, height=3, width=14, bg= "#FCF8C0", cursor="hand1")
    btnentre.pack()

    btnnoapto =  Button (ventana2, text= "NO para menores", command= chistes, height=3, width=14, bg= "#FCF8C0", cursor="hand1")
    btnnoapto.pack()
    

#################################
#TERCERA FINESTRA
def juegos():
    global ventana3
    ventana3 = Tk()
    ventana3.title ("Los juegos de CriPaBot")
    ventana3.geometry ('311x200')    
    ventana3.config(bg = "#0C5D7D")

#FUNCIONS TERCERA FINESTRA (JOCS)
    def snake():
        ventana3.destroy()
        global SNAKE

###########
#QUARTA FINESTRA (SNAKE)
        pygame.display.init() 
        SNAKE = pygame.display.set_mode((300, 300)) 
        clear = SNAKE.copy() 
        sizepoint = 10 

        dir = 1 
        snake = [(15, 15)] 
        apple = [(5, 5)] 
        main_clock = pygame.time.Clock() 
        while True: 
            for eventos in pygame.event.get(): 
                if eventos.type == QUIT: 
                    pygame.quit() 
                    os.sys.exit(0) 
                elif eventos.type == KEYDOWN: 
                    print(eventos.key) 
                    if eventos.key == 273: 
                        dir = 1 
                    elif eventos.key == 274: 
                        dir = 2 
                    elif eventos.key == 275: 
                        dir = 3 
                    elif eventos.key == 276: 
                        dir = 4        
            SNAKE.blit(clear, (0, 0))         
            for node in snake: 
                x, y = node 
                pygame.draw.rect(SNAKE, (255, 255, 255), ((x * sizepoint, y * sizepoint), (sizepoint, sizepoint)), 1) 
            x, y = apple[0]     
            pygame.draw.rect(SNAKE, (255, 0, 0), ((x * sizepoint, y * sizepoint), (sizepoint, sizepoint)), 1) 
            if dir == 1: 
                x, y = snake[0] 
                y -= 1 
                y = 29 if y < 0 else y 
                snake.insert(0, (x, y)) 
            elif dir == 2: 
                x, y = snake[0] 
                y += 1 
                y = 0 if y > 29 else y 
                snake.insert(0, (x, y)) 
            elif dir == 3: 
                x, y = snake[0] 
                x += 1 
                x = 0 if x > 29 else x 
                snake.insert(0, (x, y)) 
            elif dir == 4: 
                x, y = snake[0] 
                x -= 1 
                x = 29 if x < 0 else x 
                snake.insert(0, (x, y)) 
            if snake[0] in snake[1:]: 
                print("Has perdido") 
                pygame.quit() 
                os.sys.exit(0) 
            if not snake[0] in apple: 
                snake.pop(len(snake) - 1) 
            else: 
                apple.pop(0) 
                apple.append((random.randint(0, 29), (random.randint(0, 29))))   
            main_clock.tick(10) 
            pygame.display.flip() 

#################################
#FINESTRA JOC NUMEROS
#CREAR LA PRIMERA FINESTRA DE L'APLICACIÓ
    def adivina():
        ventana3.destroy()
        global ventana4
        ventana4 = Toplevel()
        ventana4.title ("ADIVINA EL NÚMERO")
        ventana4.geometry ('350x300')
        ventana4.config( bg= "#74D5E8")

        etiketablanc=Label(ventana4, text = "", bg= "#74D5E8")
        etiketablanc.pack()

        etiketa11=Label(ventana4, text = "Bienvenido a 'ADIVINA EL NÚMERO'", bg= "#74D5E8")
        etiketa11.pack()

        etiketablanc11=Label(ventana4, bg= "#74D5E8" ,text = "Tienes que adivinar un número de entre 1 y 50,")
        etiketablanc11.pack()
        etiketa12= Label(ventana4, text= "ambos incluidos. ¡Adelante!", bg= "#74D5E8")
        etiketa12.pack()

        etiketablanc5=Label(ventana4, text = "", bg= "#74D5E8")
        etiketablanc5.pack()

        etiketa2= Label(ventana4, text = "Realiza tus intentos...", bg= "#74D5E8")
        etiketa2.pack()

        etiketablanc6=Label(ventana4, text = "", bg= "#74D5E8")
        etiketablanc6.pack()

        global valor
        valor = IntVar()
        caja = Entry(ventana4, textvariable = valor)
        caja.pack()

        etiketablanc3=Label(ventana4, text = "", bg= "#74D5E8")
        etiketablanc3.pack()
        
        r = random.randrange(1,51)
        global numero_intentos
        numero_intentos=1

        def probar(r):
            global valor
            global valor2
            global intento
            global numero_intentos
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
            numero_intentos= numero_intentos+1  
             

        boton1 = Button(ventana4, text="Probar", bg="#2F89F5", height= 3, width= 6, command= lambda:probar(r))
        boton1.pack()

        etiketablanc7=Label (ventana4, text = "", bg= "#74D5E8")
        etiketablanc7.pack()

        global valor2
        valor2=StringVar()
        eiketa3 =Label(ventana4, textvariable = valor2, bg= "#74D5E8")
        eiketa3.pack()

        global valor3
        valor3=StringVar()
        eiketa89 =Label(ventana4, textvariable = valor3, bg= "#74D5E8")
        eiketa89.pack()

#CAIXES I ETIKETES TERCERA FINESTRA
    etiketaintrov2 = Label (ventana3, text= "Buena elección!", bg= "#FCF8C0")
    etiketaintrov2.pack()

    etiketaintrov22 = Label (ventana3, text= "Elije juego", bg= "#FCF8C0")
    etiketaintrov22.pack()

    etiketabl1 = Label ( ventana3, text= "", bg= "#0C5D7D")
    etiketabl1.pack()
    
    btnsnake = Button (ventana3, text= "Snake", command=snake, height=3, width=14, bg= "#FCF8C0", cursor="hand1")
    btnsnake.pack()
    
    btnadiv = Button (ventana3, text= "Puedes adivinar el número?", command=adivina, height=3, width=20, bg= "#FCF8C0", cursor="hand1")
    btnadiv.pack()

#################################
#PRIMERA FINESTRA
ventana1 = Tk()
ventana1.title ("Conecta CriPaBot")
ventana1.geometry ('313x471')

filename = PhotoImage(file = "galaxiab.gif")
background_label = Label(ventana1,image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#ventana1.mainloop()

#etiketa blanca
etiketab1 = Label ( ventana1, text= "", bg= "#000000")
etiketab1.pack()

etiketab2 = Label ( ventana1, text= "", bg= "#000000")
etiketab2.pack()

#USUARI
etiketau = Label (ventana1, text= "Usuario CriPaBot:")
etiketau.pack()
global valor1
valor1=StringVar()
cajau = Entry(ventana1, textvariable=valor1)
cajau.pack()

#etiketa blanca
etiketab = Label ( ventana1, text= "", bg= "#000000")
etiketab.pack()

#CONTRASSENYA
etiketap = Label ( ventana1, text= "Contaseña:")
etiketap.pack()
global valor2
valor2=StringVar()
cajap = Entry(ventana1, textvariable=valor2, show = "*")
cajap.pack()

#etiketa blanca
etiketab3 = Label ( ventana1, text= "", bg= "#000000")
etiketab3.pack()

#BOTONS    
botonlog = Button(ventana1, text="LogIn", command = usuarios, height=2, width=4,cursor="hand1")
botonlog.pack()

#etiketa blanca
etiketab7 = Label ( ventana1, text= "", bg= "#FFFFFF")
etiketab7.pack()

etiketah1 = Label ( ventana1, text= "Aún no eres usuario de CriPaBot?")
etiketah1.pack()

etiketah2 = Label ( ventana1, text= "Hazte una cuenta!")
etiketah2.pack()

#etiketa blanca
etiketab6 = Label ( ventana1, text= "", bg= "#FFFFFF")
etiketab6.pack()

botonnr = Button(ventana1, text="Nuevo usuario", command = nuevo, height=2, width=9, cursor="hand1")
botonnr.pack()

#BOTONS
#etiketa blanca
etiketab5 = Label ( ventana1, text= "", bg= "#FFFFFF")
etiketab5.pack()

botoncer = Button(ventana1, text="Cerrar", command = ventana1.destroy, height=2, width=4, cursor="hand1")
botoncer.pack()
