import random 
 
def acertarNumero(): 
    num = random.randint(0, 100) 
    inten = 0 
     
    while True: 
        x = int(input("Introduzca número: ")) 
        if x == num: 
            print("Acertaste; " + str(inten) + "intentos") 
            return 0 
        elif x < num: 
            print("El número que buscas es mayor.") 
            inten = inten + 1 
        else:  
            print("El número que buscas es menor.") 
            inten = inten + 1 
             
acertarNumero() 
