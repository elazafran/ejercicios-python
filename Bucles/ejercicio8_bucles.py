'''

8. Usando for, haz que Python escriba todas las tablas de multiplicar, del 1 al 10:
el formato que ha de tener la solución es el siguiente con las 10 tablas, titulo de la tabla que se
esta realizando y el formato ejemplo 1*9=9
Tabla de multiplicar del 9
1 * 9 = 9
2 * 9 = 18
3 * 9 = 27
4 * 9 = 36
5 * 9 = 45
Ejercicios practico con bucle while y for
6 * 9 = 54
7 * 9 = 63
8 * 9 = 72
9 * 9 = 81
10 * 9 = 90

'''


for i in range (1,10+1):
    for j in range (1,10+1):
        print i,"*",j,"=",i*j

