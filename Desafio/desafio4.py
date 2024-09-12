# Digitando a Lista de Compras
frutas = ["maça" , "banana" , "laranja"]
print("Lista de frutas:" , frutas)

# Solicitando ao usuário uma nova fruta
novafruta = input("Digite uma nova fruta aqui: ")

# Adicionando nova fruta
frutas.append(novafruta)
print("Lista de frutas atualizada: " , frutas)

# Removendo uma fruta
frutaRemover = input("Digite a fruta que quer remover: ")

if frutaRemover in frutas:
    frutas.remove(frutaRemover)
    print("Lista de frutas atualizada final", frutas)
else:
    print("Fruta não está na lista para ser removida")