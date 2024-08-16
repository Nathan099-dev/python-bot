import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Vale demais aprender a linguagem python, pois com ela você consegue construir muitas coisas interessntes')

    if resposta == '2':
        print(f''' 
        Alguns projetos que são possíveis de se fazer usando a linguagem python:
        1 - Chatbots
        2 - Automação de tarefas
        3 - Dashboards interativos e completos
        4 - Ferramentas focadas em segurança da informação
        5 - Ferrametas de análise de dados 
        6 - calculadora
        7 - jogos
        8 - conversor de moedas
        ''')

    if resposta == '3':
         print(f'{os.linesep}{nome} Você pode sim começar sua jornada  no mundo da  programação usando a  linguagem python, pois ela é uma linguagem siplesdese  entender e, por isso, perfeita para quem está começando.')
       

def start():
    #apresentar o bot
    print('Olá! Bem-vindo  ao bot')

    #solicitar o nome do  usuário
    nome = ''
    str(input('Digite o seu  nome'))

    #enviar uma msg de boas vindas
    print(f'Bem-vindo, {nome}!')

    while True:
            resposta = input(f'O que  você gostaria de saber hoje? \n{os.linesep} [1] Vale a pena aprender a linguagem python? \n{os.linesep} [2] O que  posso construir usando a linguagem python? \n {os.linesep} [3] Posso começar a estudar python como minha primeira linguagem de programação ou preciso escolher outra para entrar na área')


    #processar a resposta
    processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
