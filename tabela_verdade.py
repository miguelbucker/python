a = 2
b = 6
c = 3

operacaoAnd = a == b and c * a == b
print (operacaoAnd)
operacaoOr = a == b or c * a == b
print (operacaoOr)

operacaoAnd2 = a == (c + b) and b == c
print(operacaoAnd2)
operacaoOr2 = a == (c + b) or b == c
print(operacaoOr2)

operacaoAnd3 = a > 5 and b > 3
print(operacaoAnd3)
operacaoOr3 = a > 5 or b > 3
print(operacaoOr3)

operacaoAnd4 = a < 5 and c >= 3
print(operacaoAnd4)
operacaoOr4 = a < 5 or c >= 3
print(operacaoOr4)

operacaoAnd5 = not b == 6 and 3 * 2 == b
print(operacaoAnd5)
operacaoOr5 = not b == 6 or 3 * 2 == b
print(operacaoOr5)

operacaoAnd6 = c < 5 and not b > 6
print(operacaoAnd6)
operacaoOr6 = c < 5 or b > 6
print(operacaoOr6)