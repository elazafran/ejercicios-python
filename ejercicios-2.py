# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario, el resultado tendrá dos decimales
 

# Almacenar Notas
nota1 = input("Introduce la nota 1: ")
nota2 = input("Introduce la nota 2: ")
nota3 = input("Introduce la nota 3: ")
nota4 = input("Introduce la nota 4: ")

# Definimos funcion para calcular la media
def nota_media():
        
        todas_notas= nota1+nota2+nota3+nota4
        resultado= todas_notas/4
        return format(resultado,".2f")

resultado_final=nota_media()

""" Imprime las notas """
print("Nota 1:", nota1 )
print("Nota 2:", nota2 )
print("Nota 3:", nota3 )
print("Nota 4:", nota4 )
print("Nota media", resultado_final)

