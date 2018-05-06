'''

12. Escribe un programa que dados dos números, uno entero positivo (base) y un
entero positivo (exponente), saque por pantalla el resultado de la potencia. No se
puede utilizar el operador de potencia (**). Ejemplo 23 sera 2*2*2


'''
 
base = int(raw_input("uno entero positivo (base)"))
exponente = int(raw_input("un entero positivo (exponente)"))
resultado =1
for i in range(1,exponente+1):
    resultado = base * resultado
    
print " resultado igual %d"%(resultado)

