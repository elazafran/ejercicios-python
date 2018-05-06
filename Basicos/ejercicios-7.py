
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Ejemplo 1000minutos= 16 horas y 40 minutos


# Guardamos los datos del usuario
#minutos  = float(raw_input("minutos a convertir: "))


""" Imprime los datos """

num=int(raw_input("ingrese los minutos\n"))
hor=(int(num/60))
minu=int((num-(hor*60)))

print(str(hor)+"h "+str(minu)+"m ")




