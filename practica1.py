#---------------------------EJERCICIO 1--------------------

x = input('INGRESE UN VALOR PARA PARA PIRAMIDE: ')

for i in range(int(x)):

        print("*"*(i+1))


#--------------------------EJERCICIO 2 --------------------


z = int(input('INGRESE UN NUMERO:'))
while z < 0:
    print( "Los números negativos no son permitidos ")
    z = int(input('VUELVA A INGRESAR UN NUMERO:')) 


for i in range(z,-1,-1):
     print(i,"   ",end="")

        
#----------------------Ejercicio3---------------------------
   
z = int(input('INGRESE UN NUMERO ENTERO:'))

for n in range(2, z):
        if z % n == 0:
            print("No es primo")
            z = int(input('INGRESE UN NUMERO ENTERO:'))
            
print("Es primo")

 
    

        



