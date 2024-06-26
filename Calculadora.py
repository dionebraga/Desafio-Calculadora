def calculadora(operacao, num1, num2):
    match operacao:
        case "adicao":
            return num1 + num2
        case "subtracao":
            return num1 - num2
        case "multiplicacao":
            return num1 * num2
        case "divisao":
            return num1 / num2
        case _:
            return "Operação inválida"

def main():
    print("Escolha a operação: adicao, subtracao, multiplicacao, divisao")
    operacao = input("Digite a operação: ").strip().lower()
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calculadora(operacao, num1, num2)
    print(f"O resultado da {operacao} é: {resultado}")

if __name__ == "_main_":
    main()

    # main
    