#juegos A
m=int(raw_input("Juegos del jugador A: "))
#juegos B
n=int(raw_input("Juegos del jugador B: "))

if((m>0) and (n>0)) and ((n<8) and (m<8)):
    
    if ((n==6)and(m==7)) or ((m==6)and(n<5)) or ((m-n)==2) and (m>5):
        print("gana A")
    elif((m==6) and (n==7)) or ((n==6)and(m<5)) or ((n-m)==2) and (n>5):
        print("gana B")
    elif(m<6) and (n<6):
        print("el set todavía no termina")
    elif((m>6)and(n<5)) or ((n>6)and(m<5)):
        print("resultado inválidoooo")
    else:
        print("resultado invalidado")
else:
    print("resultado es inválido ")
