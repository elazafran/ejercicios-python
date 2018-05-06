'''

7. Escribe un programa en IDLE que escriba aquellos números entre 1 y 100 que:
Sean pares
No sean múltiplos de 4
Tampoco sean múltiplos de 3.


'''

for i in range (1,101):
    #print i
    if i%2==0 and (i%3!=0) and (i%4!=0):
            print i

