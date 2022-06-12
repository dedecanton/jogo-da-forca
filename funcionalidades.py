
from os import system


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
    elif (dicasInformadas > 2):
        print(f'Todas as dicas já foram informadas')
    print('*'*50)


def chutar(palavra_chave, letras_acertadas, letras_faltando, erros, chutes):
    chute = pede_letra()

    if not chute or len(chute) != 1:
        print('Letra inválida')
        chutar(palavra_chave, letras_acertadas, letras_faltando, erros, chutes)

    chutes.append(chute)
    if chute in palavra_chave:
        print('Acertou!')
        for index, letra in enumerate(palavra_chave):
            if chute == letra:
                letras_acertadas[index] = chute
        letras_faltando = str(letras_acertadas.count('_'))
    else:
        print('Errou :(')
        erros += 1
    return letras_acertadas, int(letras_faltando), int(erros), chutes


def escrever_resultado(resultado):
    doc = open('resultados.txt', 'a')
    doc.writelines(resultado)


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


def mostrar_mensagem_derrota():
    print('Você perdeu :(')


def mostrar_mensagem_vitoria():
    print('Você ganhou!')


def mostrar_informacoes_jogo(letras_acertadas, erros, chutes):
    print(f'Progresso: {letras_acertadas}')
    print(f'Erros: {erros}')
    print(f'Chutes: {chutes}')
