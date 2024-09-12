# Pesquisar no dicionário
listaAluno = {"Miguel": 8 , "Carol": 10}
print("A lista de alunos e suas notas é: ", listaAluno)

# Solicitando o nome do aluno 
nomeAluno = input("Digite aqui o nome do aluno: ")

# Mostrando a nota na tela
if nomeAluno in listaAluno:
    print(f"A nota do aluno é: {listaAluno[nomeAluno]}")
else:
    print("Aluno não está na lista")


