import pandas as pd

df = pd.read_excel('xlsx')
colunas = ['colunas que deverão ser binarizadas(PELO NOME)']

df[colunas] = df[colunas].apply(lambda x: pd.Series(pd.factorize(x)[0])).astype('category')

df.to_excel('caminho_do_novo_arquivo.xlsx', index=False)