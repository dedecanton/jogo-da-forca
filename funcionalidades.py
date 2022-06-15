
from os import system
from time import sleep

def pular_linha():
    print('\n')

def limpar_tela():
    system('clear') # if system is windows, change "clear" to "cls"

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_letra():
    return input('Digite uma letra: ')


def informar_dica(dicasInformadas, dica1, dica2, dica3):
    print('*'*50)
    if (dicasInformadas == 0):
        print(f'Dica 1: {dica1}')
    elif (dicasInformadas == 1):
        print(f'Dica 2: {dica2}')
    elif (dicasInformadas == 2):
        print(f'Dica 3: {dica3}')
    elif (dicasInformadas >= 3):
        print(f'Todas as dicas já foram informadas')
    print('*'*50)


def chutar(palavra_chave, letras_acertadas, letras_faltando, erros, chutes):
    chute = pede_letra()

    if not chute or len(chute) != 1 or chute.isnumeric():
        print('Letra inválida')
        return chutar(palavra_chave, letras_acertadas, letras_faltando, erros, chutes)

    chutes.append(chute)
    if chute in palavra_chave:
        for index, letra in enumerate(palavra_chave):
            if chute == letra:
                letras_acertadas[index] = chute
        letras_faltando = str(letras_acertadas.count('_'))
    else: 
        erros += 1
    
    limpar_tela()
    return letras_acertadas, int(letras_faltando), int(erros), chutes


def escrever_resultado(palavra_chave, ganhador, perdedor):
    doc = open('resultados.txt', 'a')
    doc.writelines(f'Palavra: {palavra_chave} | Ganhador: {ganhador} | Perdedor: {perdedor} \n')


def historico_de_partidas():
    try:
        doc = open('resultados.txt', 'r')
        text = doc.read()
        print(f'{"*"*20} Histórico de partidas {"*"*20} \n')
        print(text)
        print("*"*63)
    except:
        print('*'*50)
        print('Não há resultados')
        print('*'*50)


def jogar_novamente(functionGame):
    historico_de_partidas()

    opcao = input('Digite (S) para jogar novamente ou (N) para sair: ')
    opcao = opcao.lower()

    if(opcao == 's'):
        system('clear')
        functionGame()
    elif(opcao == 'n'):
        quit()
    else:
        print('Operação inválida')
        jogar_novamente(functionGame)


def mostrar_mensagem_derrota():
    pular_linha() 
    print(f'{"*" * 20} Você perdeu :( {"*" * 20}')
    pular_linha()
    
def mostrar_mensagem_vitoria():
    pular_linha()
    print(f'{"*" * 20} Você ganhou :) {"*" * 20}')
    pular_linha()
    


def mostrar_informacoes_jogo(letras_acertadas, erros, chutes):
    print(f'Progresso: {letras_acertadas}')
    print(f'Erros: {erros}')
    print(f'Chutes: {chutes}')
