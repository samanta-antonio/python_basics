#Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
n = int(input("Digite o valor de n: "))

i = 1
fatoração = 1

while i <= n:
    fatoração = fatoração * i
    i = i + 1

print(fatoração)
  
