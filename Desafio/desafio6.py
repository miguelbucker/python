# Manipulação de dicionário/objetos

dadosLivro = {"título": "Dom Casmurro" , "autor": "Machado de Assis" , "Ano": 1899 }
print("Dados do Livro: " , dadosLivro)

# Solicitando o novo ano
novoAno = input("Digite o novo ano aqui: ")

dadosLivro["Ano"] = novoAno
print("Dados Livro Atualizado" , dadosLivro)
