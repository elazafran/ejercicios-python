'''
8.Introducir cadenas hasta que el usuario no desea insertar más en una lista.
Para cada cadena se imprimiera el siguiente mensaje dependiendo de su longitud .

Si la longitud es menor de 5 pondrá el nombre de la cadena y que es menor que 5
y en caso contrario pondrá que es mayor que 5 y la cadena

Juan menor que 5
Juancarlos mayor que 5

'''
cadena = raw_input("indroduzca cadena :\n")
while cadena!=" ":
    
    if len(cadena)>5:
        print "'%s' es mayor que 5"%cadena
    else:
        print "'%s' es menor que 5"%cadena
    cadena = raw_input("Indroduzca cadena :\n")


'''
profe manu
'''
lista=[]
continuar="s"
while continuar=="s":
    cade= raw_input("introduce cadena")
    lista.append(cad)
    continuar= raw_input("quiees continuar s/n")
for i in lista:
    if len(i)<5:
        print i, " es menor de 5"
    if len(i)>5:
        print i, " es mayor de 5"
