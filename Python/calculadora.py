# CALCULADORA SIMPLES

# Criando as variáveis.

valor1 = 0
valor2 = 0
operacao = ''
resultado = 0

# Colocando o while para fazer o loop, assim quando terminar de mostrar o resultado da operação, ele vai voltar ao começo e pedir um novo valor novamente.

while True:

# Entrada de dados do usuário.
    
    valor1 = int(input('Digite um valor: '))
    operacao = input('Digite a operação: ')
    valor2 = int(input('Digite um valor: '))

# Condição para validar a operação.

    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        resultado = valor1 / valor2
    elif operacao == '**':
        resultado = valor1 ** valor2
    else:
        print('Operação invalida!')
    print(resultado)
       
        

    
        