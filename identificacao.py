def pedir_identificacao():
    desafiante = input('Digite o nome do Desafiante: ')
    competidor = input('Digite o nome do Competidor: ')
    
    if(not desafiante or not competidor):
        print('Você inseriu algum valor inválido')
        pedir_identificacao()

    return [desafiante, competidor]
