from re import X
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#DATAFRAME

vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
produtos_df = pd.read_csv(r"data\Contoso - Cadastro Produtos.csv", sep=";")
lojas_df = pd.read_csv(r"data\Contoso - Lojas.csv", sep=";")
clientes_df = pd.read_csv(r"data\Contoso - Clientes.csv", sep=";")
promocoes_df = pd.read_csv(r"data\Contoso - Promocoes.csv", sep=";")


#DROP LIXO

clientes_df = clientes_df.drop(clientes_df.columns[[7, 8, 9, 10]], axis=1)
promocoes_df = promocoes_df.drop(promocoes_df.columns[[5, 6]], axis=1)


#MERGE

vendas_df = vendas_df.merge(produtos_df, on="ID Produto")
vendas_df = vendas_df.merge(lojas_df, on="ID Loja")
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")


# RESULTADO
#frequencia_clientes = vendas_df[["Primeiro Nome", "Sobrenome", "E-mail"]].value_counts()
frequencia_clientes = vendas_df[["E-mail"]].value_counts()
frequencia_produtos = vendas_df[["ID Produto","Nome do Produto"]].value_counts()
#display(frequencia_produtos[:5])
display(frequencia_clientes[:5])
#display(vendas_df["Quantidade Vendida"].info())
#display(vendas_df.sort_values(by="Quantidade Vendida", ascending=False).head(5))

#display(produtos_df)
#display(lojas_df)
#display(clientes_df)
#display(promocoes_df)

#display(vendas_df.nlargest(5, "Quantidade Vendida")[["Primeiro Nome", "Sobrenome", "E-mail", "Quantidade Vendida"]])

# PLOT

frequencia_clientes = frequencia_clientes[:5]
#plt.hist(frequencia_clientes)
frequencia_clientes.plot()
plt.show()

