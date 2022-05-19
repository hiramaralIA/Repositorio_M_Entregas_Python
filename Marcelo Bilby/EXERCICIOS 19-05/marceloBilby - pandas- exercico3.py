import pandas as pd

vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
produtos_df = pd.read_csv(r"data\Contoso - Cadastro Produtos.csv", sep=";")
lojas_df = pd.read_csv(r"data\Contoso - Lojas.csv", sep=";")
clientes_df = pd.read_csv(r"data\Contoso - Clientes.csv", sep=";")
vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
print(vendas_df)