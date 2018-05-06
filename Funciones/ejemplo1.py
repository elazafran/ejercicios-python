def introducir_datos():
    lado = int(raw_input("introduce lado"))
    superficie(lado)

def superficie(lado):
    area = lado*lado
    print area
    
#bloque principal
introducir_datos()
    
