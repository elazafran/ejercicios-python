s=raw_input('Inserte una cadena: ')
ch='.'
new=''
cont=0
for i in s[::-1]:
   if cont!=0 and cont%3==0:
       new=new+ch
   new=new+i
   cont=cont+1
print new[::-1]
