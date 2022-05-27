# IMPORT PACKAGES

import pandas as pd
from prompt_toolkit import formatted_text
from IPython.display import display


# DATAFRAME

funcionarios_df = pd.read_csv('data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('data/BaseServiçosPrestados.xlsx')

# ADD NEW COLUMN "SALARIO TOTAL"

funcionarios_df["Salario Total"] = funcionarios_df["Salario Base"] + funcionarios_df["Impostos"] + funcionarios_df["Beneficios"]

# RESULT

total = funcionarios_df["Salario Total"].sum()
porcentagem = total * 0.1
reajuste = total + porcentagem

print(f"Valor da folha de pagamento: {total:,.2f}")
print(f"Folha com reajuste de 10%: {reajuste:,.2f}")
