num1=float(raw_input("Introduzca numero 1: "))
num2=float(raw_input("Introduzca numero 2: "))
operador = raw_input("Introduzca un operador (+,-,*,/): ")

if((operador is "+") or (operador is "-") or (operador is "*") or (operador is "/")):
    if(operador is "+"):
        result=num1+num2
        print "La suma es: {0:.2f}".format(result)
    elif (operador is "-"):
        result=num1-num2
        print "La resta es: {0:.2f}".format(result)
    elif(operador is "*"):
        result=num1*num2
        print "La multiplicacion es: {0:.2f}".format(result)
    elif(operador is "/"):
        if(num2>0):
            result=num1/num2
            print "La division es: {0:.2f}".format(result)
        else:
            print "No se puede realizar la operacion"       
else:
    print("Operador incorrecto")
    
#mostremos signo del resultado, si es positivo o negativo
if(result<0)or(result<0):
    print("Resultado negativo")
else:
    print("Resultado positivo")
