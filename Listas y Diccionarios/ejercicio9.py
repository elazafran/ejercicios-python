'''
9.Introduce por teclado 5 números mételos en una lista
y suma los elementos de la lista por ultimo muestra la lista,
la media de la suma, y la suma.

'''
lista=[]
resultado=0
for i in range(5):
    cadena = int(raw_input("indroduzca numero :\n"))
    resultado +=cadena
    lista.append(cadena)

print lista
media = resultado/float(len(lista))
print media
print "%d esta es la suma y esta es la media %f"%(resultado,resultado/float(len(lista)))
