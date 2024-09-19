# Calculadora Simples
def calcular(op,numero1,numero2):
    if op == "somar":
        soma = numero1 + numero2
        return soma
    elif op == "subtrair" :
        subtracao = numero1 - numero2
        return subtracao
    elif op == "multiplicar" :
        multiplicacao = numero1 * numero2
        return multiplicacao
    elif op == "dividir" :
        divisao = numero1 / numero2
        return divisao

def main():
    listaOperacoes = ["somar","subtrair","multiplicar","dividir"]
    numero1 = float(input("Digite o 1º número para calcular: "))
    numero2 = float(input("Digite o 2º número para calcular: "))
    op = input("Digite qual operacao quer realizar: ")

    if op.lower() not in listaOperacoes:
        print("Operação Inválida!")
        novamente = input("Deseja tentar novamente? (S/N)").upper()

        if(novamente == "S"):
            main()
        else:
            print("Programa está sendo finalizado")
        return

    resultado = calcular(op,numero1,numero2)

    if isinstance(resultado,str):
        print(resultado)
    else:
        print(f"O resultado de {numero1} {op} {numero2} é {resultado} ")

main()



