# IMPORT PACKAGES

import pandas as pd

# DATAFRAME

funcionarios_df = pd.read_csv('./data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('./data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('./data/BaseServiçosPrestados.xlsx')

# MERGE CLIENTES_DF AND SERVICOS_DF

empresa_df = servicos_df.merge(clientes_df, on="ID Cliente")

# CREATE NEW VARIABLE MEDIAMENSAL

empresa_df["Faturamento Total"] = (empresa_df["Valor Contrato Mensal"] * empresa_df["Tempo Total de Contrato (Meses)"])
mediaMensal = empresa_df["Faturamento Total"].mean()
mediaMensal = f"{mediaMensal:_.2f}"
mediaMensal = mediaMensal.replace("_", ".")

# RESULT

print(f"Media Mensal: {mediaMensal}")