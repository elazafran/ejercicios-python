'''
1. Crea una aplicación que permita adivinar un número. En primer lugar la aplicación
solicita un número entero por teclado y otro que será el número adivinar. A continuación
va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el
introducido. El programa termina cuando se acierta el número. Usar While
'''

nSecreto = int(raw_input("Introduzca número secreto: "))
#nUsuario=int(raw_input("Introduzca número: "))
boleano = False
while (boleano == False):
    nUsuario = int(raw_input("Introduzca numero nuevamente "))
    if nSecreto == nUsuario:
        boleano=True
        print("ha acertado!!")
    elif nSecreto > nUsuario:
        
        print("el numero es menor a adivinar")
    else :
        print("el numero es mayor a adivinar")
   




