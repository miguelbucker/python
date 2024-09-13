# Calculadora Simples
def calculos(numero1,numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    return (soma, subtracao, multiplicacao, divisao)

# Solicitar ao usuário os números para serem calculados
numero1 = float(input("Digite o 1º número para calcular: "))
numero2 = float(input("Digite o 2º número para calcular: "))


