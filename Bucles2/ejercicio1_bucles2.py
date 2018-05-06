'''
1.Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores obtenidos.
Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de combinaciones de dados con las que se puede obtener ese puntaje.

'''
dado1=1
dado2=1

#sumatotal=4
sumatotal= int (raw_input("indrouzca un numero para calcular sus combinaciones"))
for i in range(1, 7):
    dado1=i
    for j in range(1,7):
        dado2=j
        if dado1+dado2 == sumatotal :
           print("dado1 su valor", dado1, "+", dado2, " resultado =", sumatotal )
        
