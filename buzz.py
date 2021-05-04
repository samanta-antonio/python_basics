#Receba um número inteiro na entrada e imprima Buzz, se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input("Digite um número: "))

resto = (numero % 5)

if resto == 0:
    print("Buzz")
else:
    print(numero)
    
