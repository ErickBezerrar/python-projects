import pandas as pd

# Carrega os dados do histórico de preços da ação
dados = pd.read_csv('dados_precos_acao.csv')

# Define os critérios de avaliação (média móvel de 50 dias e média móvel de 200 dias)
dados['MA50'] = dados['Close'].rolling(window=50).mean()
dados['MA200'] = dados['Close'].rolling(window=200).mean()

# Define a regra de decisão: se a média móvel de 50 dias é maior que a média móvel de 200 dias, então é um bom momento para comprar
if dados['MA50'].iloc[-1] > dados['MA200'].iloc[-1]:
    print("É um bom momento para comprar a ação!")
else:
    print("Não é um bom momento para comprar a ação.")
