'''

9. Pide un número por teclado
y que se muestre la tabla de multiplicar de dicho número(for)
'''

tablade = int(raw_input("introduzca numero para su tabla "))

for i in range (1,10+1):
    print i,"*",tablade,"=",(i*tablade)

