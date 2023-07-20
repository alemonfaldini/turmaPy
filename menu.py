from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import InicialFinal
from exercicio07 import impares
from exercicio08 import somarInteiro
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio09 import lerSomar
from exercicio10 import calcularMedia
from exercicio11 import maiorMenor
from exercicio12 import positivoNegativo
from exercicio13 import fatorial
from exercicio14 import mediaVolei
from exercicio15 import miss
from exercicio16 import eleicao



def mostrarMenu():
    print('\n\n\n Escolha uma das opções abaixo: ' +
            '\n0. SAIR'        +
            '\n1. Exercicio 01'+
            '\n2. Exercicio 02'+
            '\n3. Exercicio 03'+
            '\n4. Exercicio 04'+
            '\n5. Exercicio 05'+
            '\n6. Exercicio 06'+
            '\n7. Exercicio 07'+
            '\n8. Exercicio 08'+
            '\n9. Exercicio 09'+
            '\n10.Exercicio 10'+
            '\n11.Exercicio 11'+
            '\n12.Exercicio 12'+
            '\n13.Exercicio 13'+
            '\n14.Exercicio 14'+
            '\n15.Exercicio 15'+
            '\n16.Exercicio 16'+
            '\n17.Exercicio 17'+
            '\n18.Exercicio 18'+
            '\n19.Exercicio 19'+
            '\n20.Exercicio 20' +
            '\n21. Preencher Vetor' +
            '\n22. Consultar Vetor ' +
            '\n23. Apagar posição Vetor')


def operacao ():
    #Chamar o método de cima
    opcao = 1 #Instanciar = Dar um valor inicial
    while(opcao != 0):
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))

        #Executo a ação
        if (opcao ==0):
            #Instruções do exercício 01
            return 'Obrigado!'
        elif(opcao==1):
            return
        elif(opcao==2):
            return
        elif(opcao==3):
            return
        elif(opcao==4):
            #Utilizar exercicio 04
            print('\nexercicio04')
            print(somarInteiro())
        elif(opcao==5):
            #Exercicio05
            print('\nExercicio 05')
            num=int(input('Informe o numero'))
            n=coletarPositivo()
            tabuada(num,n)
        elif (opcao ==6):
            # Exercicio06
            print('\nExercicio 06')
            inicio = int(input('Informe o inicio'))
            fim = int(input('Informe o fim'))
            InicialFinal(inicio,fim)
        elif (opcao ==7):
            # Exercicio07
             print('\nExercicio 07')
             impares()
        elif (opcao ==8):
            # Exercicio08
            print('\nExercicio 08')
            print(somarInteiro())
        elif (opcao ==9):
            #Exercicio09
            print('\nExercicio 09')
            print(lerSomar())
        elif(opcao ==10):
            #Exercicio10
            print('\nExercicio10')
            print(calcularMedia())
        elif (opcao ==11):
            #Exercicio11
            print ('\nexercicio11')
            print(maiorMenor())

        elif (opcao == 12):
            #Exercicio12
            print ('\nexercicio12')
            print (positivoNegativo)

        elif (opcao == 13):
            #Exercicio13
            print ('\nexercicio13')
            num = int(input('Informe um numero'))
            print(fatorial(num))

        elif (opcao == 14):
            #Exercicio14
            print ('\nexercicio14')
            print (mediaVolei())


        elif (opcao == 15):
            #Exercicio15
            print('\nexercicio15')
            print (miss())


        elif (opcao == 16):
            #Exercicio16
            print('\nexercicio16')
            print (eleicao())


        elif (opcao == 17):
            #Exercicio17
            print('\nexercicio17')
        elif (opcao == 18):
            #Exercicio18
            return
        elif (opcao == 19):
            #Exercicio19
            return
        elif (opcao == 20):
            #Exercicio20
            return
        elif (opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor (num)
        elif (opcao == 22):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor (num)
        elif(opcao==23):
            posicao = int(input('Informe a posição que deseja apagar:'))
            apagarPosicao(posicao-1)
        else:
            return 'Opção escolhida não é valida, digite novamente!'


