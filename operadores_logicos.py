#declarando variaveis
dataMaxima = 28
idadeMinima = 14
idadeMaxima = 17
indicacao = True
listaEspera = False
idadeMarcelo = 15
diaInscricao = 29

if diaInscricao > dataMaxima :
    print("Marcelo tem indicacao especial")
else :
    print("Marcelo nao tem indicacao especial")

if idadeMinima < idadeMarcelo and idadeMarcelo < idadeMaxima :
    print("Marcelo pode se inscrever")
else :
    print("Marcelo nao tem idade permitida")

if listaEspera == False :
    print("Marcelo nao esta na lista de espera")
