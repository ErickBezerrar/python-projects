import pandas as pd

# leia o arquivo excel
df = pd.read_excel('')

# visualize o conteúdo do dataframe
print(df.head())

#colunas = ['colunas que deverão ser binarizadas(PELO NOME)']
#df[colunas] = df[colunas].apply(lambda x: pd.Series(pd.factorize(x)[0])).astype('category')
#df.to_excel('caminho_do_novo_arquivo.xlsx', index=False)
