'''
10.Créate una lista con las vocales y pide una palabra por teclado
si dicha palabra contiene las 5 vocales
imprime la palabra murciélago

'''
cadena = raw_input("indroduzca palabra :\n")
vocales = ["a","e","i","o","u"]
contador =0

for i in cadena:
    for j in vocales:
        if i==j:
            contador=contador+1
        
if contador==5:
    print "mucierlago"
'''
manue
'''

cadena = raw_input("indroduzca palabra :\n")
vocales = ["a","e","i","o","u"]

for vocal in vocales:
    if vocal not in palabra.lower():
        break
    else:#solo se ejecuta si el for no hace break
        prin "Probablemente has escrito 'murcielago' :-)
