import time

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

#######################

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
            print ("Que vida mas cruel te espera pues..")
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
            print ("¿Y el racismo que?")
            time.sleep(2)
        elif resp10 == "2":
            print ("¿Y el machismo que?")
            time.sleep(3)
        break
print("Gracias por jugar conmigo! Me tengo que ir, adiós! :)")
resp1=input ("¿Qué preieferes?(1/2)")
print("by: Cris Expósito y Paula Gomila")

        


                
