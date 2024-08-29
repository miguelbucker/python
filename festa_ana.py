dia = int(input("Qual o dia de hoje?"))
pedidoPizza =  int(input("Quantas pizzas comprou?"))
pedidoBebida =  int(input("Quantas bebidas comprou?"))
pedidoBolo =  int(input("Quantos bolos comprou?"))
pedidoDoce =  int(input("Quantos doces comprou?"))

# Declarando Variaveis
diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
pedidoMinimoDoce = 600

if diaFesta == dia:
    print("Ana esta fazendo as compras no dia da festa")
else:
    print("Ana esta fazendo as compras adiantado")

if (pedidoMinimoPizza >= pedidoPizza):
    print("Ana nao comprou pizzas suficientes")

if (pedidoMinimoBebida < pedidoBebida):
    print("Ana nao comprou mais bebidas que o necessario")

if (pedidoMinimoBolo <= pedidoBolo):
    print("Ana excedeu a compra de bolos!")

if (pedidoMinimoDoce > pedidoDoce):
    print("Ana nao comprou doce suficientes")