# IMPORTANDO ARQUIVOS
import pandas as pd
from IPython.display import display

# DATAFRAME

funcionarios_df = pd.read_csv('data/CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('data/CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('data/BaseServiçosPrestados.xlsx')

# DISPLAY

display(funcionarios_df)