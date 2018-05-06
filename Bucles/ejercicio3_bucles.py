'''
3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘CONSONANTE’ si no, el
programa termina cuando se introduce un espacio. Usar While

'''

entrada = raw_input("introduzca carácter: ")

while entrada != " ":
    if (entrada =="a" or entrada =="e" or entrada =="i" or entrada =="o"or entrada =="u"):
        print ("ha introducido una vocal")
    else:
        print ("ha introducido una consonante")
    entrada = raw_input("introduzca carácter: ")
    
print "ha terminado porque ha metido un espacio"
