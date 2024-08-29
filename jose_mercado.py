#José foi ao mercado com R$ 50,00
saldo_inicial = 50.00

#definindo valor do refrigerante
custo_refrigerante = 8

#definindo valor do pão
custo_pao = 4

#definindo valor da mortadela
custo_mortadela = 39.90

# calculando o total da compra 

ValorCompra = (custo_refrigerante * 2) + custo_pao + (custo_mortadela * 0.3)

#definindo saldo final e printando o resultado

Saldo_final = saldo_inicial - ValorCompra
print(f"Jose chegou com R${saldo_inicial} e saiu com R${Saldo_final} !!")
