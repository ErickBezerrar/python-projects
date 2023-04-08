import pandas as pd

# Definir valores iniciais
investimento_inicial = float(input("Digite o valor do investimento inicial: "))
aporte_mensal = float(input("Digite o valor do aporte mensal: "))
taxa_juros = 0.1  # taxa de juros anual de 10%
anos = int(input("Digite a quantidade de anos do investimento: "))

# Calcular o valor futuro do investimento
valor_futuro = investimento_inicial
dados = {"Ano": [], "Valor Futuro": []}
for i in range(anos):
    for j in range(12):  # percorrer cada mês do ano
        valor_futuro = (valor_futuro + aporte_mensal) * (1 + taxa_juros/12)  # calcular o novo valor futuro com base nos juros compostos
    dados["Ano"].append(i+1)
    dados["Valor Futuro"].append(valor_futuro)

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel
df.to_excel("investimento.xlsx", index=False)
