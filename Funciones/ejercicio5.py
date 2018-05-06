'''

6.Crea una función para calcular el IVA de un producto.
Deberá recibir un precio y devolver el precio IVA incluido.


'''

def iva(precio):

    return (precio*0.21)+precio
        

    
    
#bloque principal
precio = int(raw_input("introduce precio sin iva"))


print "el precio con iva es",iva(precio)
