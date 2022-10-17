valor = int(input("Informe um número inteiro e positivo:"))

if valor > 0:
    fatorial = 1
    for i in range(1,valor,+1):
        fatorial = fatorial * valor
    print(fatorial)
else:
    print("Rode o programa novamente e insira um número correto")