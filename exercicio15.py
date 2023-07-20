15.#Em um concurso de miss,os jurados precisam digitar o nome das 16 candidatas e
# suas respectivas notas(0a10).
# Crie um programa que leia esta sinformações e que,ao final do programa,
# apresente apenas o nome e a nota da vencedora.

def validacaoNtas():
    nota=float (input('Informe uma nota:'))
    while ((nota < 0) or (nota > 10)):
        print ('Erro!!! Informe uma nota entre 0 e 10')
        nota=float (input('Informe uma nota: '))
    return nota




def miss ():
    nomeVencedora = ''
    notaVencedora = 0

    for i in range (1, 17):
        nome = input('Informe o nome da {} ª candidata: ' .format (i))
        nota = validacaoNotas() #Números com vírgula r não negativos


    #Verificação da vencedora
        if (notaVencedora) = nota
        notaVencedora = nota
        nomeVencedora = nome

    return 'Vencedora: {}\nNota: {}' .format(nomeVencedora, notaVencedora)
