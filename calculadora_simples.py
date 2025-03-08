# Calculadora simples

"""
Calculadora, utilizando while
"""

print('Antes de entrar, quero te dar um infeliz anúncio de que nossa calculadora não comporta mais do que 2 números.')
print('Procuraremos atualizar nossos serviços o quanto antes, ainda estamos em fase de desenvolvimento. Agradeço a paciência.')

usuario = input('Olá, me diga seu nome. ')
print(f'Seja bem-vindo(a) à calculadora, {usuario}!')

condicao = True
while condicao:
    print('Para utilizar nossa calculadora, basta digitar "entrar".')
    print('Caso não deseje utilizar nossos serviços ou só veio olhar, digite "sair".')

    entrada = input('Deseja entrar ou sair? \n')
    if entrada == 'Entrar':
        while condicao:
            saida = input('Lembrando que se deseja sair, basta digitar "sair", senão continue com "continue": \n')
            if saida == 'Sair':
                break
            elif saida == 'Continue':
                print('Temos serviços para estas operações aritméticas: adição, subtração, multiplicação e divisão...'
                    'Além dessas temos: Divisão inteira, potenciação e módulo.')
                operacao = input('Qual operação deseja: \n')
                if operacao == 'Adição':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    adicao = float_num1 + float_num2
                    print(f'O resultado é: {adicao:.2f}')
                elif operacao == 'Subtração':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    subtracao = float_num1 - float_num2
                    print(f'O resultado é: {subtracao:.2f}')
                elif operacao == 'Multiplicação':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    multiplicao = float_num1 * float_num2
                    print(f'O resultado é: {multiplicao:.2f}')
                elif operacao == 'Divisão':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    divisao = float_num1 / float_num2
                    print(f'O resultado é: {divisao:.2f}')
                elif operacao == 'Divisão inteira':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    divisao_inteira = float_num1 // float_num2
                    print(f'O resultado é: {divisao_inteira:.2f}')
                elif operacao == 'Potenciação':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    potenciacao = float_num1 ** float_num2
                    print(f'O resultado é: {potenciacao:.2f}')
                elif operacao == 'Módulo':
                    numero_1 = input('Digite seu primeiro número: ')
                    numero_2 = input ('Digite seu segundo número: ')
                    float_num1 = float(numero_1)
                    float_num2 = float(numero_2)
                    modulo = float_num1 % float_num2
                    print(f'O resultado é: {modulo:.2f}')
                else:
                    print('Você tem que digitar alguma coisa ou alguma operação das operações que listamos.')
    elif entrada == 'Sair':
        print(f'Agradeço pela presença, até mais, {usuario}!')
        break
    else:
        print(f'{usuario}, você tem que digitar se deseja entrar ou sair.')
