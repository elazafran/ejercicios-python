'''
6.A partir de dos listas de enteros, 'numeros1' y 'numeros2' de igual tamaño,
generar otra cuyo primer elemento es el producto
del primer elemento de las listas 'numeros1' y 'numeros2', y así sucesivamente.

numeros1 = [1, 7, 13, 21, 27]
numeros2 = [4, 6, 10, 18, 23]
resultado=[4,42,130….]
'''

numeros1 = [1, 7, 13, 21, 27]
numeros2 = [4, 6, 10, 18, 23]
resultado=[]

for i in range(len(numeros1)):
    resultado.append(numeros1[i]*numeros2[i])
        

print "resultado:",resultado
