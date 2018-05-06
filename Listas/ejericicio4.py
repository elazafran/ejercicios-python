'''

4.Introduce números por teclado y guárdalo en una lista, el proceso finaliza cuando metamos un número negativo.
Muestra el máximo de los números guardado en la lista, muestra los números pares.
Con la función max(lista) se obtiene el mayor de la lista

'''



lista=[]
cadena = int(raw_input("diga cadena y evitaremos repetir"))

while 0<cadena:
    cadena = int(raw_input("diga cadena y evitaremos repetir"))
    if(cadena>0):    
        lista.append(cadena)    
    else:
        break
    
print max(lista)
