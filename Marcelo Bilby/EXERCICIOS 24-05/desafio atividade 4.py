# IMPORT PACKAGES

import pandas as pd

# from prompt_toolkit import formatted_text
from IPython.display import display


# DATAFRAME

funcionarios_df = pd.read_csv('./data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('./data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('./data/BaseServiçosPrestados.xlsx')

# GET SIZE TABLE FUNCIONÁRIOS AND TABLE SERVIÇOS

totalDeFuncionarios = len(funcionarios_df["ID Funcionário"].unique())
funcionariosQuePossuemContratos = len(servicos_df["ID Funcionário"].unique())

# RESULT

percentual = funcionariosQuePossuemContratos/totalDeFuncionarios
percentual = percentual * 100

print(f"O percentual de funcionários que fecharam contrato é de: {percentual:.2f} %")
print("")
print("Lista de funcionários que fecharam contrato por área: ")

totalFuncionarios = funcionarios_df["ID Funcionário"].unique()
totalContratos = servicos_df["ID Funcionário"].unique()

contratos = funcionarios_df.loc[funcionarios_df["ID Funcionário"].isin(servicos_df["ID Funcionário"])].reset_index(drop=True)


contratos = contratos["Area"].value_counts()

display(contratos)

print("Média mensal dos contratos: ")

faturamento_df =  clientes_df.merge(servicos_df, on="ID Cliente")
faturamento_df["Faturamento Total"] = faturamento_df["Valor Contrato Mensal"] * faturamento_df["Tempo Total de Contrato (Meses)"]
faturamento_df = faturamento_df["Faturamento Total"].sum() / faturamento_df["Tempo Total de Contrato (Meses)"].mean()
mediaMensal = f"{faturamento_df:_.2f}"
mediaMensal = mediaMensal.replace("_", ".")
display(mediaMensal)


