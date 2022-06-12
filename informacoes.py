def pedir_informacoes():
    palavra_chave = input('Digite a palavra chave: ')
    dica1 = input('Digite a dica 1: ')
    dica2 = input('Digite a dica 2: ')
    dica3 = input('Digite a dica 3: ')

    if(not dica1 or not dica2 or not dica3):
        print('Você inseriu algum valor inválido')
        pedir_informacoes()

    return [
        palavra_chave,
        dica1,
        dica2,
        dica3
    ]
