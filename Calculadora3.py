operation = input('''
Por favor, digite o tipo de operação que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

numero_1 = int(input('Entre com o primeiro número: '))
numero_2 = int(input('Entre com o segundo número : '))

if operation == '+':
    print('{} + {} = '.format(numero_1, numero_2))
    print(numero_1 + numero_2)

elif operation == '-':
    print('{} - {} = '.format(numero_1, numero_2))
    print(numero_1 - numero_2)

elif operation == '*':
    print('{} * {} = '.format(numero_1, numero_2))
    print(numero_1 * numero_2)

elif operation == '/':
    print('{} / {} = '.format(numero_1, numero_2))
    print(numero_1 / numero_2)

else:
    print('Você não digitou um operador válido, execute o programa novamente.')