# Variaveis de Preço
p1 = [100,200,300]

# Definindo a variavel total atraves da função soma
total = sum(p1)

# Definindo o desconto quando o valor total é maior do que 500
desconto = 0
if total > 500:
    desconto = total * 0.1

# Calculando o resultado subtraindo o desconto do valor total
resultado = total - desconto

print(f"Total antes do desconto: {total}")
print(f"Desconto aplicado: {desconto}")
print(f"Total com desconto: {resultado}")