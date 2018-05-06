'''

3.Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.
Ejemplo si introducimos caracola se imprimirá carol

'''
cadena = raw_input("diga cadena y evitaremos repetir")
lista=[]

#print len(cadena)

for i in range (len(cadena)):
    
    agregar=cadena[i]
    
    if agregar in lista:
        print "existe"
    else :
        lista.append(agregar)    
    
    
print lista
