import os
from random import randint

cores = ['azul', 'verde', 'amarelo', 'vermelho', 'preto', 'laranja', 'cinza', 'roxo']


def criaPadrao():
    padrao = []
    for i in range(4):
        indice = randint(0, 7)
        if (cores[indice] != ''):
            padrao.append(cores[indice])
        else:
            if i > 0:
                i = i - 1

    return padrao


def execTentativas(tentativas):
    tentativas.append([])
    for interator in range(4):
        os.system('cls')
        print('CORES: ')
        for i in range(8):
            print(' [' + cores[i] + '] - numero: ', i)
        tentativas[len(tentativas) - 1].append(
            cores[int(input('\nDigite o numero correpondente a cor da casa ' + str(interator) + ': '))])

    return tentativas


def verPainel(padrao, tentativas, resultados):
    os.system('cls')

    if len(tentativas) == 10:
        print('\nPADRAO CORRETO: {} | {} | {} | {} '.format(padrao[0], padrao[1], padrao[2], padrao[3]))
        print('\n\n')
    else:
        print('\nO PADRÃO CORRETO SERÁ EXIBIDO APÓS A DECIMA TENTATIVA!!\n')
    for i in range(len(tentativas)):
        print('TENTATIVA   {}: {} | {} | {} | {} | RESULTADOS: {} {} {} {} '.format(i + 1, tentativas[i][0],
                                                                                    tentativas[i][1], tentativas[i][2],
                                                                                    tentativas[i][3], resultados[i][0],
                                                                                    resultados[i][1], resultados[i][2],
                                                                                    resultados[i][3]))
    input("APERTE ENTER")


def criarFeedback(padrao, tentativas, resultados):
    for i in range(len(tentativas)):
        resultados.append([])
        for j in range(len(tentativas[i])):
            resultados[i].append('')

    for c in range(len(tentativas)):
        for i in range(len(tentativas[c])):
            for j in range(len(padrao)):
                if (tentativas[c][i] == padrao[j]) and (tentativas[c][i] != ''):
                    if i == j:
                        resultados[c][i] = 'Bola preta'

    for c in range(len(tentativas)):
        for i in range(len(tentativas[c])):
            for j in range(len(padrao)):
                if (tentativas[c][i] == padrao[j]) and (tentativas[c][i] != ''):
                    if i != j:
                        resultados[c][i] = 'Bola branca'
    return resultados


def main():
    padrao = criaPadrao()
    tentativas = []
    feedback = []
    for i in range(10):
        tentativas = execTentativas(tentativas)
        feedback = criarFeedback(padrao, tentativas, feedback)

        verPainel(padrao, tentativas, feedback)
        if padrao in tentativas:
            print('ACERTOU TODAS AS CORES')
            input()
            main()

    main()


main()
