# Exercício - Sistema de perguntas e respostas

perguntas = [
    {'Matemática': [
        {
            'Pergunta': 'Quanto é 2+2?',
            'Opções': ['1', '3', '4', '5'],
            'Resposta': 'C',
        },
        {
            'Pergunta': 'Quanto é 5*5?',
            'Opções': ['25', '55', '10', '51'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Quanto é 10/2?',
            'Opções': ['4', '5', '2', '1'],
            'Resposta': 'B',
        },
    ]},
    {'Geografia': [
        {
            'Pergunta': 'Qual a capital do Brasil?',
            'Opções': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Belo Horizonte'],
            'Resposta': 'C',
        },
        {
            'Pergunta': 'Qual a capital da Argentina?',
            'Opções': ['Buenos Aires', 'Córdoba', 'Rosário', 'Mendoza'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Qual a capital da França?',
            'Opções': ['Paris', 'Lyon', 'Marselha', 'Toulouse'],
            'Resposta': 'A',
        }
    ]},
    {'História': [
        {
            'Pergunta': 'Quem descobriu o Brasil?',
            'Opções': ['Pedro Álvares Cabral', 'Cristóvão Colombo', 'Vasco da Gama', 'Bartolomeu Dias'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Em que ano o Brasil foi descoberto?',
            'Opções': ['1500', '1492', '1530', '1499'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Quem foi o primeiro presidente do Brasil?',
            'Opções': ['Getúlio Vargas', 'Deodoro da Fonseca', 'José Sarney', 'Luís Inácio Lula da Silva'],
            'Resposta': 'B',
        }
    ]},
    {'Ciências': [
        {
            'Pergunta': 'Qual a fórmula da água?',
            'Opções': ['H2O', 'CO2', 'H2SO4', 'H2O2'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Qual a fórmula do ácido sulfúrico?',
            'Opções': ['H2O', 'CO2', 'H2SO4', 'H2O2'],
            'Resposta': 'C',
        },
        {
            'Pergunta': 'Qual a fórmula do peróxido de hidrogênio?',
            'Opções': ['H2O', 'CO2', 'H2SO4', 'H2O2'],
            'Resposta': 'D',
        }
    ]},
    {'Português': [
        {
            'Pergunta': 'Qual a função sintática da palavra "João" na frase "João gosta de sorvete"?',
            'Opções': ['Sujeito', 'Predicado', 'Objeto direto', 'Objeto indireto'],
            'Resposta': 'A',
        },
        {
            'Pergunta': 'Qual a função sintática da palavra "sorvete" na frase "João gosta de sorvete"?',
            'Opções': ['Sujeito', 'Predicado', 'Objeto direto', 'Objeto indireto'],
            'Resposta': 'C',
        },
        {
            'Pergunta': 'Qual a função sintática da palavra "de sorvete" na frase "João gosta de sorvete"?',
            'Opções': ['Sujeito', 'Predicado', 'Objeto direto', 'Objeto indireto'],
            'Resposta': 'D',
        },
    ]}
]

respostas_certas = 0
input('Bem-vindo ao quiz! Pressione enter para começar...')

for tema in perguntas:
    for chave, lista_perguntas in tema.items():
        print(f"\nTema: {chave}")
        for pergunta in lista_perguntas:
            print(f"\n{pergunta['Pergunta']}")
            print('Opções:')
            opcoes = ['A', 'B', 'C', 'D']
            for i, opcao in enumerate(pergunta['Opções']):
                print(f'[{opcoes[i]}] {opcao}')
            resposta = input('Sua resposta: ').upper()
            if resposta == pergunta['Resposta']:
                print('Parabéns! Você acertou!')
                respostas_certas += 1
            else:
                print('Que pena! Você errou!')

print(f'\nVocê acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {respostas_certas / sum(len(tema[chave]) for tema in perguntas for chave in tema) * 100:.2f}%.')
