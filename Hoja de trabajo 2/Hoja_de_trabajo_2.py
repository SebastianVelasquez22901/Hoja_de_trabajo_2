
def Arbol(n):
    return "\n".join([" "*(n-i)+"*"*(i+i-1) for i in range(1,n+1)])

print("-------------------------------------------------------------")
num_asteristcos=int(input("Escriba el numero de niveles que desee que tenga el arbol: "))
print("-------------------------------------------------------------")
print(Arbol(num_asteristcos))

print("--------------Parte dos de la hoja--------------")
def PRIMO(num):
    for n in range(2, num):
        if num % n == 0:
            print("-------------------------------------------------------------")
            print("No es numero primo")
            print("-------------------------------------------------------------")
            return False
    print("Es un numero primo")
    return True
 
num=int(input("Escriba su numero para ver si es primo: "))
PRIMO(num)

