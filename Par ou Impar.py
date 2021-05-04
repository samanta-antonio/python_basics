#Receba um número inteiro na entrada e imprima, par, quando o número for par ou  ímpar quando número for ímpar.

numero = int(input("Digite um número para saber se é par ou ímpar: "))

resto = (numero % 2)

if resto == 0:
    print("par")
else:
    print("ímpar")
