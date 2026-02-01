# Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Qual a capital do Brasil?',
        'opcoes': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'resposta': 2
    },
    {
        'pergunta': 'Quem descobriu o Brasil?',
        'opcoes': ['Pedro Álvares Cabral', 'Cristóvão Colombo', 'Vasco da Gama', 'Fernando de Magalhães'],
        'resposta': 0
    },
    {
        'pergunta': 'Qual o maior planeta do sistema solar?',
        'opcoes': ['Terra', 'Júpiter', 'Saturno', 'Urano'],
        'resposta': 1
    }

]

respostas_certas = 0

for pergunta in perguntas:
    print(pergunta['pergunta']) # Exibe a pergunta
    for i, opcao in enumerate(pergunta['opcoes']):# Exibe as opções
        print(f'{i}) {opcao}')# Exibe as opções
    resposta_usuario = int(input('Digite o número da resposta: '))# Lê a resposta do usuário
    if resposta_usuario == pergunta['resposta']:# Verifica a resposta
        print('Resposta correta!\n')# Incrementa o contador de respostas certas
        respostas_certas += 1# Exibe o resultado final
    else:
        print('Resposta incorreta!\n') # Exibe o resultado final
    print(f'Você acertou {respostas_certas} de {len(perguntas)} perguntas.')