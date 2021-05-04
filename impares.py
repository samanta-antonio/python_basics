#Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais.

n = int(input("Digite o valor de n: "))

i = 1
contador = 1
if n == 0:
    print(i)
else:
    while contador <= n:
        print(i)
        i = i+2
        contador = contador + 1


    
