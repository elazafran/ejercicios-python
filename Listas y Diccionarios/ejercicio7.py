'''
7.A partir de dos listas de enteros, 'numeros1' y 'numeros2', almacenar en una lista el resultado de multiplicar cada uno de los elementos de 'numeros1'  por todos los elementos de numeros2. 
numeros1 = [1, 7, 13, 21, 27]
numeros2 = [8, 9, 28, 41, 55, 77]

'''
numeros1 = [1, 7, 13, 21, 27]
numeros2 = [8, 9, 28, 41, 55, 77]

resultado=[]

for i in numeros1:
    for j in numeros2:
        resultado.append(i*j)
        

print "resultado:",resultado
