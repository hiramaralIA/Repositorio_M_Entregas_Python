# IMPORT PACKAGES

import pandas as pd

# from prompt_toolkit import formatted_text
from IPython.display import display

def retornaValorReal(valor):
    valor = f'{valor:_.2f}'
    valor = valor.replace('_', '.')
    return valor


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
print("Lista de funcionários que não fecharam contrato: ")

totalFuncionarios = funcionarios_df["ID Funcionário"].unique()
totalContratos = servicos_df["ID Funcionário"].unique()

naoFecharamContrato = funcionarios_df.loc[~funcionarios_df["ID Funcionário"].isin(servicos_df["ID Funcionário"])].reset_index(drop=True)


display(naoFecharamContrato)


