#8. Escrever um algoritmo que leia 10
    #numeros inteiros e, ao final, apresente a
    #soma de todos os números lidos;

def somarInteiro():
      soma = 0
      for i in range(1,11,1):
         num = int(input('{} ° numero: '.format(i)))
         soma += num

      return 'A soma dos números digitados foi {}'.format(soma)
