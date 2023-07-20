#10 Escreva um algoritmo que calcule a média dos números
# digitados pelo usuário,se eles forem pares.
# Termine a leitura se o usuário digitar zero(0);

def calcularMedia():
    num = 1
    soma = 0
    contador = 0

    while(num!=0):
        num = int(input('Informe um número:'))

        if (num % 2== 0):
          soma += num
          contador += 1

    return 'A soma dos pares digitados é: {}' .format(soma/contador)
