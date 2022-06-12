from os import system
from identificacao import pedir_identificacao
from informacoes import pedir_informacoes
from funcionalidades import escrever_resultado, historico_de_partidas, inicializa_letras_acertadas, chutar, informar_dica, jogar_novamente, mostrar_informacoes_jogo, mostrar_mensagem_derrota, mostrar_mensagem_vitoria


def JogoDaForca():
    desafiante, competidor = pedir_identificacao()
    system('clear')  # if system is windows, change of "clear" to "cls"

    palavra_chave, dica1, dica2, dica3 = pedir_informacoes()
    system('clear')  # if system is windows, change of "clear" to "cls"

    # game infos
    letras_acertadas = inicializa_letras_acertadas(palavra_chave)
    dicasInformadas = 0
    enforcou = False
    ganhou = False
    letras_faltando = len(letras_acertadas)
    erros = 0
    chutes = []

    while (not enforcou and not ganhou):
        # jogo deve acabar ou não
        if erros >= 5:
            enforcou = True
            mostrar_mensagem_derrota()
            escrever_resultado(
                f'Palavra: {palavra_chave} | Perdedor: Competidor {competidor} | Ganhador: Desafiante {desafiante} \n')
            jogar_novamente(JogoDaForca)
            break

        if letras_faltando == 0:
            ganhou = True
            mostrar_mensagem_vitoria()
            escrever_resultado(
                f'Palavra: {palavra_chave} | Perdedor: Desafiante {desafiante} | Ganhador: Competidor {competidor} \n')
            jogar_novamente(JogoDaForca)
            break

        # opcoes
        mostrar_informacoes_jogo(letras_acertadas, erros, chutes)
        escolha = input(
            'Digite (1) para jogar ou (2) para pedir uma dica (no máximo 3): ')

        # jogar
        if escolha == '1':
            letras_acertadas, letras_faltando, erros, chutes = chutar(
                palavra_chave, letras_acertadas, letras_faltando, erros, chutes)
            system('clear')
        # dicas
        elif escolha == '2':
            informar_dica(dicasInformadas, dica1, dica2, dica3)
            dicasInformadas += 1
            letras_acertadas, letras_faltando, erros, chutes = chutar(
                palavra_chave, letras_acertadas, letras_faltando, erros, chutes)
            system('clear')
        else:
            print('Operação inválida!')


JogoDaForca()
