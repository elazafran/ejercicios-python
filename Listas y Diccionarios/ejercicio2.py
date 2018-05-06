'''
2. Lee valores del usuario hasta que teclee un numero par,
utilizando un bucle while

'''
a=int(input("ingrese un numero\n"))

while a%2!=0:
     print(str(a)+" es impar")
     a=int(input("ingrese un numero\n"))

print(str(a)+" es par")
