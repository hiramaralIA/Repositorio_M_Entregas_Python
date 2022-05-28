# IMPORT PACKAGES

import pandas as pd

# from prompt_toolkit import formatted_text
from IPython.display import display


# DATAFRAME

funcionarios_df = pd.read_csv('./data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('./data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('./data/BaseServiçosPrestados.xlsx')

# GET TABLE FUNCIONÁRIOS IN "Area"

funcionariosPorArea = funcionarios_df["Area"].value_counts()

# RESULT

display(funcionariosPorArea)


