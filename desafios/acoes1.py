import yfinance as yf
import pandas as pd

# Entrada do usuário
acao = input("Digite o código da ação que deseja analisar: ")

# Coletando dados da ação
acao = yf.Ticker(acao)
historico = acao.history(period="10y")

# Calculando P/PV
pp_pv = acao.info["priceToBook"]
print(f"P/PV: {pp_pv:.2f}")

# Calculando DY
dy = historico["Dividends"].sum() / historico["Close"].iloc[0] * 100
if dy < 8:
    print("DY abaixo de 8%. Análise encerrada.")
else:
    print(f"DY: {dy:.2f}%")

    # Calculando cotação
    cotacao = historico["Close"].iloc[-1]
    print(f"Cotação: R${cotacao:.2f}")

    # Análise de compra ou não
    if cotacao < historico["Close"].mean():
        print("Boa oportunidade de compra.")
    else:
        print("Não é um bom momento para compra.")
