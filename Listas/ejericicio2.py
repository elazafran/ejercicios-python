'''

2. Pide un número por teclado y guarda en una lista su tabla de multiplicar hasta el 10.
Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

'''
numero = int(raw_input("diga numero para mostrar su tabla de multiplicar "))
lista=[]


for i in range(1,11):
    resultado = numero*i    
    lista.append(resultado)
    
print lista
