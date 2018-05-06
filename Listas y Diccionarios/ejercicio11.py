'''
11.Dada la siguiente lista.Se pide crear una agenda con las siguientes opciones
Contacto=[“juan”,”pedro”,”luis”,”maria”,”natalia”]
Se le preguntara que opción desea hacer y dependiendo de la que sea se hara una cosa  u otra.
No se usara menu

A)Op1(insertar)=Se insertaran elementos a la lista siempre que no exista en caso de que exista se pondrá un msj que diga elemento ya existe
B)Op2(borrar)=Se mostrará por pantalla los elementos de la lista y se le preguntara que elemento de la lista se quiere borrar. Si el elemento no existe se pondrá un msj que diga que no existe
C)Op3=Ver lista de contactos
D)op4=salir
E)Se puede hacer con if anidados 

'''

contacto=["juan","pedro","luis","maria","natalia"]

while(True):
    cadena = raw_input("qué opción desea?: \n")
    if cadena=="op1":
        introducir = raw_input("diga elemento a insertar: \n")
        if contacto.count(introducir)==0:
            contacto.append(introducir)
        else:
            print"elemento ya existe, no se introducira"
    elif cadena=="op2":
        print contacto
        introducir = raw_input("diga elemento a borrar: \n")
        if contacto.count(introducir)!=0:
            contacto.remove(introducir)
            print contacto
        else:
            print"elemento no existe, no se borrará"
    elif cadena=="op3":
        print contacto
    elif cadena=="op4":
        break;

print contacto
