# IMPORT PACKAGES

from unicodedata import decimal
import pandas as pd
from prompt_toolkit import formatted_text
from IPython.display import display

def retornaValorReal(valor):
    valor = f'{valor:_.2f}'
    valor = valor.replace('_', '.')
    return valor


# DATAFRAME

funcionarios_df = pd.read_csv('data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('data/BaseServiçosPrestados.xlsx')

# MERGE CLIENTES_DF AND SERVICOS_DF ON "ID_CLIENTE"

faturamento_df = clientes_df.merge(servicos_df, on="ID Cliente")

# ADD NEW COLUMN "FATURAMENTO TOTAL"

faturamento_df["Faturamento Total"] = faturamento_df["Valor Contrato Mensal"] * faturamento_df["Tempo Total de Contrato (Meses)"]

# RESULT 

faturamentoTotal = faturamento_df["Faturamento Total"].sum()
faturamentoTotal = retornaValorReal(faturamentoTotal)
print(f"Faturamento total em R$: {faturamentoTotal}")
print("")
print("5 Maiores Faturamentos:")
print("")
display(faturamento_df.sort_values(by="Faturamento Total", ascending=False).head(5))
