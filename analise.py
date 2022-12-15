import pandas as pd

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados

print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
#
## quantidade de produtos vendidos por loja
#quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade)
#
#print('-' * 50)
## ticket médio por produto em cada loja
#ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
#ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
#print(ticket_medio)