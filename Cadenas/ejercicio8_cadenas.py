'''


8.Crear un programa que lea por teclado una cadena y un carácter,
e inserte el carácter entre cada letra de la cadena.
Ej: separar y , debería devolver s,e,p,a,r,a,r 

'''

cad=raw_input("Numero:")
car=raw_input("Caracter:")
cont=0
cad2=""
for c in cad:
    if cont!=0 and cont%1==0:
        cad2=cad2+car
    
    cad2=cad2+c
    cont=cont+1    

print cad2

