import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Vale demais aprender a linguagem python, pois comm ela você consegue construir muitas coisas interessntes')
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
         print(f'{os.linesep}{nome} Você pode simcomeçar sua  jornada  no mundo da  programação usando a  linguagem python, pois ela é uma linguagem siplesdese  entender e, por isso, perfeita para quem está começando.')
       

