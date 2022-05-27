import pandas as pd
from IPython.display import display

vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
#print(vendas_df[["ID Produto", "Quantidade Vendida", "Quantidade Devolvida"]])
display(vendas_df[["ID Produto", "Quantidade Vendida", "Quantidade Devolvida"]])