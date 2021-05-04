#Receba um número inteiro na entrada e imprima FizzBuzz, na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.


numero = int(input("Digite um número: "))

resto1 = (numero % 3)
resto2 = (numero % 5)

if resto1 == 0 and resto2 == 0:
    print("FizzBuzz")
else:
    print(numero)
    
