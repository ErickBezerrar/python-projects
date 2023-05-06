import pandas as pd


investimento_inicial = float(input("Digite o valor do investimento inicial: "))
aporte_mensal = float(input("Digite o valor do aporte mensal: "))
taxa_juros = 0.1  #10% ao ano.
anos = int(input("Digite a quantidade de anos do investimento: "))

valor_futuro = investimento_inicial
dados = {"Ano": [], "Valor Futuro": []}
for i in range(anos):
    for j in range(12): 
        valor_futuro = (valor_futuro + aporte_mensal) * (1 + taxa_juros/12) 
    dados["Ano"].append(i+1)
    dados["Valor Futuro"].append(valor_futuro)

df = pd.DataFrame(dados)

df.to_excel("investimento.xlsx", index=False)
