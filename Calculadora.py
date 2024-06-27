def calculadora(operacao, num1, num2):
    match operacao:
        case 'adicao':
            return num1 + num2
        case 'subtracao':
            return num1 - num2
        case 'multiplicacao':
            return num1 * num2
        case 'divisao':
            if num2 == 0:
                return "Erro: divisão por zero."
            return num1 / num2
        case _:
            return "Operação inválida."

# Exemplo de uso
if __name__ == "_main_":
    main()