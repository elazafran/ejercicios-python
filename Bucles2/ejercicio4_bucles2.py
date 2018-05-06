'''
4.Escriba un programa que entregue la suma de los primeros nn números naturales, siendo nn ingresado por el usuario.
Matemáticamente lo que se pide que haga el programa es realizar la siguiente sumatoria.
∑i=1ni=1+2+3+4+5+6+⋯+n
Además, obtenga el resultado de la siguiente fórmula.
S2=n×(n+1)/2
El programa debe entregar el resultado diciendo si S1S1 y S2S2 son iguales o no.


'''

entrada = int (raw_input("indrouzca un numero natural : "))
resultado=0
for i in range(0,entrada+1):
    resultado = resultado+i

n=entrada
S2=(n*(n+1))/2

if S2==resultado:
    print "resultado", resultado," y ",S2, "son iguales"
else:
    print "resultado", resultado," y ",S2, "son DISTintos"
