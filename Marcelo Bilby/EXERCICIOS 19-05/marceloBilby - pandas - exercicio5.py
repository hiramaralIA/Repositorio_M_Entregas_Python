import pandas as pd
from IPython.display import display

#DATAFRAME

vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
produtos_df = pd.read_csv(r"data\Contoso - Cadastro Produtos.csv", sep=";")
lojas_df = pd.read_csv(r"data\Contoso - Lojas.csv", sep=";")
clientes_df = pd.read_csv(r"data\Contoso - Clientes.csv", sep=";")
vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")

#MERGE

vendas_df = vendas_df.merge(produtos_df, on="ID Produto")
vendas_df = vendas_df.merge(lojas_df, on="ID Loja")
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")

vendas_df.drop(vendas_df.columns[[9, 10]], axis=1)

display(vendas_df)
