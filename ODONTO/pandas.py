import pandas as pd

df = pd.read_csv('nome_do_arquivo.csv')

df.head()
df.tail()
df.info()

df['nome_da_coluna']
df[df['nome_da_coluna'] == valor]
df.sort_values('nome_da_coluna')

df.groupby('nome_da_coluna').função_de_agregação()
df['nome_da_nova_coluna'] = valores_da_nova_coluna
