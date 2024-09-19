def adicionarContato(listaContato,pessoa):
    listaContato.append(pessoa)

def quantidade_contatos(listaContato):
    return len(listaContato)

def main():
    contatos = []

    print(f"Minha lista de contatos atualmente tem {quantidade_contatos(contatos)}")

    pessoaAlice = {"nome": "Alice", "telefone": "123-456-789"}
    pessoaBob = {"nome": "Bob", "telefone": "987-321-456"}

    adicionarContato(contatos, pessoaAlice)
    print(f"Minha lista de contatos atualmente tem {quantidade_contatos(contatos)}")
    print(f"Lista de contatos atualizada: {contatos}")

    adicionarContato(contatos, pessoaBob)
    print(f"Minha lista de contatos atualmente tem {quantidade_contatos(contatos)}")
    print(f"Lista de contatos atualizada: {contatos}")


main()