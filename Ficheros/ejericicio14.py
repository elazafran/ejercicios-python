'''

    14. Función que recibe un numero y devuelve una lista con todos sus divisores(return)

'''

def divisores(numero):
    resultado=[]
    for i in range(1,numero+1):
        if numero%i==0:
            resultado.append(i)
            print(i)
    print(resultado)
    return resultado

numero=int(input("introduzca numeros"))
divisores(numero)

