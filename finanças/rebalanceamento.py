import pandas as pd
import numpy as np

ativos = []

while True:
    nome = input("Insira o nome do ativo (ou 'fim' para terminar): ")
    if nome == 'fim':
        break
    quantidade = float(input("Insira a quantidade atual do ativo: "))
    preco = float(input("Insira o preço atual do ativo: "))
    ativos.append({'nome': nome, 'quantidade': quantidade, 'preco': preco})

for ativo in ativos:
    porcentagem = float(input(f"Insira a porcentagem desejada para {ativo['nome']}: "))
    ativo['porcentagem'] = porcentagem

valor_total = sum([ativo['quantidade'] * ativo['preco'] for ativo in ativos])
for ativo in ativos:
    porcentagem_atual = (ativo['quantidade'] * ativo['preco'] / valor_total) * 100
    ativo['porcentagem_atual'] = porcentagem_atual
    if porcentagem_atual < ativo['porcentagem']:
        porcentagem_desejada = ativo['porcentagem']
        quantidade_atual = ativo['quantidade']
        preco_atual = ativo['preco']
        quantidade_adicional = (porcentagem_desejada / 100) * valor_total - quantidade_atual * preco_atual
        ativo['quantidade_adicional'] = quantidade_adicional
    else:
        ativo['quantidade_adicional'] = 0

df = pd.DataFrame(ativos)
df = df[['nome', 'quantidade', 'preco', 'porcentagem', 'porcentagem_atual', 'quantidade_adicional']]
df = df.loc[df['quantidade_adicional'] > 0]
print(df)
