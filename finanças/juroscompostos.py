# Definir valores iniciais
investimento_inicial = float(input("Digite o valor do investimento inicial: "))
aporte_mensal = float(input("Digite o valor do aporte mensal: "))
taxa_juros = 0.1  # taxa de juros anual de 10%
anos = int(input("Digite a quantidade de anos do investimento: "))


valor_futuro = investimento_inicial
for i in range(anos):
    for j in range(12):  # percorrer cada mês do ano
        valor_futuro = (valor_futuro + aporte_mensal) * (1 + taxa_juros/12) 
    print("Ano {}: R$ {:.2f}".format(i+1, valor_futuro)) 
