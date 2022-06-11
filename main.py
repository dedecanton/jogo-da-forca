from identificacao import pedir_identificacao
from informacoes import pedir_informacoes

while True:
    desafiante, competidor = pedir_identificacao()
    palavra_chave, dica1, dica2, dica3 = pedir_informacoes()
