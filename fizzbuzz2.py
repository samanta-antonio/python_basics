#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve, 'Fizz' se o número for divisível por 3 e não for divisível por 5; 'Buzz' se o número for divisível por 5 e não for divisível por 3; 'FizzBuzz' se o número for divisível por 3 e por 5; Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.


def fizzbuzz(n):

    resto1 = (n % 3)
    resto2 = (n % 5)

    if resto1 == 0 and resto2 != 0:
        return("Fizz")

    if resto2 == 0 and resto1 != 0:
        return("Buzz")

    if resto1 == 0 and resto2 == 0:
        return("FizzBuzz")

    else:
        return(n)
