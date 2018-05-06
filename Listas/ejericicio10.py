'''
10.Tenemos un restaurante con la siguiente lista=[“juan”,”pedro”,”domingo”]
Pedir por teclado el nombre de las personas que van llegando y comprobar que están en la lista.
Si están imprimiremos se dejan pasar y si no están  en la lista imprimirá usted no está invitado

'''

lista=["juan","pedro","domingo"]

while(True):
    nombreAcomprobar =  raw_input("introduzca nombre : ")    
    if nombreAcomprobar in lista:
        print "puede pasar"
    elif nombreAcomprobar==" ":
        break;
        
    else:
        print "NO puede pasar"
        

