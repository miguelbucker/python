frutas = ["maca" , "banana" , "laranja"]
print("Lista de frutas:",  frutas)

frutas.append("uva")
print("Lista de frutas atualizada:", frutas)

print("Primeira fruta:", frutas[0])
print("Terceira fruta:", frutas[3])

frutas.remove(frutas[2])
print(frutas)

pessoa = {"nome": "Ana" , "idade": 30}
print("Pessoa:" , pessoa)

print("Nome:", pessoa["nome"])

pessoa["cidade"] = "São Paulo"
print("Pessoa atualizada:", pessoa)

listaPessoas = []

pessoa = {"nome": "Ana", "idade": 32}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa = {"nome": "Brenda", "idade": 26}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa = {"nome": "Fernanda", "idade": 48}
listaPessoas.append(pessoa)
print(listaPessoas)

a = {1,2,3}
b = {3,4,5}

print(a & b)
print(a | b)
print(a - b)

conjunto = {1,2,3,4,5}
print(3 in conjunto)
print(6 in conjunto)



