#Receba 3 números inteiros na entrada e imprima crescente, se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente.


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a <= b and b <= c:
    print("Crescente")
else:
    print("Não está em ordem crescente")
