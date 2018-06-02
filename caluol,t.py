def calcu():
    global app
    #CREAR LA PRIMERA FINESTRA DE L'APLICACIÓ
    app = Tk ()

    #CAMBIAR COLOR DE LA FINESTRA
    app.config(bg="#113096")

    #TITOL I MIDA DE LA FINESTRA
    app.title ("CALCULADORA")
    app.geometry ('185x250')

    #FUNIONS BOTONS 
    def btnClic(n):
        add=v.get()
        v.set(add+str(n))

    def btnIgual():
        op=v.get()
        resultat = str(eval(op))
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
        v.set("HOLA!")

    def ayuda():
        v.set("Clica los botones ")
        
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

#MENÚ
    #1.barra menu
    barramenu = Menu(app)
    #2.crear menú
    menuArchivo= Menu(barramenu)
    #3.crear archius dins menu
    menuArchivo.add_command(label="Hola", command=lambda:saludo())
    menuArchivo.add_command(label="Ayuda", command=lambda:ayuda())
    menuArchivo.add_command(label="Limpiar", command=lambda:clear())
    menuArchivo.add_command(label="Cerrar", command=app.destroy)
    #4.afegir els menus a la barra de menus
    barramenu.add_cascade(label="Más...", menu=menuArchivo)
    #5.indicar que la barra de menus estirà en la finestra
    app.config(menu=barramenu)
    

    #CAIXA ON SORTIRAN ELS NUMEROS
    v = StringVar()
    caixa2 = Entry(app, textvariable=v, width=21)
    caixa2.grid(column=1, row=1, columnspan=4)

    intronum = StringVar()
    caixa = Entry(app, textvariable=intronum, width=21)
    caixa.grid(column=1, row=2, columnspan=4)

    #CREAR BOTONS suma resta...
    botonclear = Button(app, text="Limpiar", height=2, width=3, command = lambda:btnClear(), bg="#FFFFFF" ,cursor="hand1")
    botonclear.grid(column=1, row=3, columnspan=2)

    botonans = Button(app, text="Ans", height=2, width=3, command = lambda:btnAns(), bg="#FFFFFF" ,cursor="hand1")
    botonans.grid(column=3, row=3, columnspan=4)

    botons = Button(app, text="+", command=lambda:btnClic("+"), height=2, width=2, bg="#FFFFFF" ,cursor="hand1")
    botons.grid(column=4, row=4)

    botonr = Button(app, text="-", command=lambda:btnClic("-"), height=2, width=2, bg="#FFFFFF" ,cursor="hand1")
    botonr.grid(column=4, row=5)

    botonm = Button(app, text="*", command=lambda:btnClic("*"), height=2, width=2, bg="#FFFFFF", cursor="hand1")
    botonm.grid(column=4, row=6)

    botond = Button(app, text="/",command=lambda:btnClic("/"),  height=2, width=2, bg="#FFFFFF" ,cursor="hand1")
    botond.grid(column=4, row=7)

    #CREAR BOTONS numeros..
    boton7 = Button(app, text="7",command=lambda:btnClic(7),  height=2, width=2, bg="#6680FF",cursor="hand1")
    boton7.grid(column=1, row=4)

    boton8 = Button(app, text="8", command=lambda:btnClic(8), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton8.grid(column=2, row=4)

    boton9 = Button(app, text="9", command=lambda:btnClic(9), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton9.grid(column=3, row=4)

    boton4 = Button(app, text="4", command=lambda:btnClic(4), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton4.grid(column=1, row=5)

    boton5 = Button(app, text="5", command=lambda:btnClic(5), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton5.grid(column=2, row=5)

    boton6 = Button(app, text="6", command=lambda:btnClic(6), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton6.grid(column=3, row=5)

    boton1 = Button(app, text="1",command=lambda:btnClic(1),  height=2, width=2, bg="#6680FF",cursor="hand1")
    boton1.grid(column=1, row=6)

    boton9 = Button(app, text="2", command=lambda:btnClic(2), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton9.grid(column=2, row=6)

    boton3 = Button(app, text="3", command=lambda:btnClic(3), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton3.grid(column=3, row=6)

    boton9 = Button(app, text="0", command=lambda:btnClic(0), height=2, width=2, bg="#6680FF",cursor="hand1")
    boton9.grid(column=2, row=7)

    botonig = Button(app, text="=", command=lambda:btnIgual(), height=2, width=2, bg="#6699FF",cursor="hand1")
    botonig.grid(column=3, row=7)

    botoncom = Button(app, text=",", command=lambda:btnClic(","), height=2, width=2, bg="#6699FF",cursor="hand1")
    botoncom.grid(column=1, row=7)



    #DARRERA ETIQUETA ON SORTIRÀ EL TEXT ESCRIT DINS LA CAIXA
    respostasum = StringVar()
    etiketa2 = Label (app, textvariable=respostasum)
    etiketa2.grid()
