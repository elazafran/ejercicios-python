'''
3.Escriba un programa que permita determinar el número mayor y menor perteneciente a un conjunto de n números,
donde tanto el valor de n como el de los números deben ser ingresados por el usuario.
Ejemplo 5 
1,1,-1,-2,3  
Mayor 3
Menor -1


'''
numero_mayor =0
numero_menor =0

entrada=1
while entrada!=0:
    entrada = int (raw_input("indrouzca un numero entero : "))
    if(entrada>numero_mayor):
        numero_mayor=entrada
    if(entrada<numero_menor):
        numero_menor=entrada

print "numero_mayor", numero_mayor
print "numero_menor : ",numero_menor
