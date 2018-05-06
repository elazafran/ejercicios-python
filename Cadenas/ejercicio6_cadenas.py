'''

6.Crear un programa que lea por teclado una cadena y un carácter, e inserte el caracter cada 3 dígitos en la cadena.
Ej. 2552552550 y . debería devolver 255.255.255.0 

'''


cadena=raw_input("introduzca una cadena:")
caracter=raw_input("introduzca un caracter:")
cadenafinal=""
cont=0

for i in cadena:
  
    if(cont==3):
        print "entro una vez"
        cadenafinal=cadenafinal+caracter+i
        cont=0
        
    elif cont!=3:    
        cadenafinal=cadenafinal+i
    cont=cont+1
    
print cadenafinal
print "----"

