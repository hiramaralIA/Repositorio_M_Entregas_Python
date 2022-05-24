import pandas as pd
from tqdm import tqdm
from IPython.display import display


#DATAFRAME

vendas_df = pd.read_csv(r"data\Contoso - Vendas  - 2017.csv", sep=";")
produtos_df = pd.read_csv(r"data\Contoso - Cadastro Produtos.csv", sep=";")
lojas_df = pd.read_csv(r"data\Contoso - Lojas.csv", sep=";")
clientes_df = pd.read_csv(r"data\Contoso - Clientes.csv", sep=";")
promocoes_df = pd.read_csv(r"data\Contoso - Promocoes.csv", sep=";")


# RESULTADO

pbar = tqdm(total=len(vendas_df["ID Loja"]), position=0, leave=True)
for i, id_loja in enumerate(vendas_df["ID Loja"]):
    pbar.update()
    if id_loja == 222:
        vendas_df.loc[i, "Quantidade Devolvida"] += 1
display(vendas_df)