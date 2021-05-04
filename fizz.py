#Receba um número inteiro na entrada e imprima Fizz se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input("Digite um número: "))

resto = (numero % 3)

if resto == 0:
    print("Fizz")
else:
    print(numero)
    
