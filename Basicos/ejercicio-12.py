
estatura=float(raw_input("Introduzca altura en metros (1.68): "))
peso=float(raw_input("Introduzca peso en kg: "))
edad=int(raw_input("Introduzca edad: "))

IMC=peso/estatura**2
print "Su IMC es: {0:.2f}".format(IMC)

if(edad<45):
    if(IMC<22.0):
        print("Mensaje: bajo")
    else:
        print("Mensaje: medio")
else:
    if(IMC<=22.0):
        print("Mensaje: medio")
    else:
        print("Mensaje: alto")
