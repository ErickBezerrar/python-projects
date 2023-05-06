import pandas as pd
import matplotlib.pyplot as plt

start_date = '2020-01-01'
end_date = '2023-04-16'

symbol = 'AAPL'

df = pd.read_csv(f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1=1577836800&period2=1689792000&interval=1d&events=history&includeAdjustedClose=true')


df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]


plt.plot(df['Date'], df['Close'])
plt.title(f'Histórico de preços de fechamento da Apple ({start_date} a {end_date})')
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.show()
