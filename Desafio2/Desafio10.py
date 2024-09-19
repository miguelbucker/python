def manipularString(texto):

    textoMaiusculo = texto.upper()
    textoMinusculo = texto.upper()
    totaisCaracteres = len(texto)

    return (textoMaiusculo,textoMinusculo,totaisCaracteres)

def main():
    palavra = input("Digite uma string para ser manipulada: ")

    