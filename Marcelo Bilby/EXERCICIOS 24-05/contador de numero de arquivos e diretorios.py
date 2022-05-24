import os


PATH = 'E:/'

contadorDeArquivos = 0
contadorDeDiretorios = 0

for root, dirs, files in os.walk(PATH):
    print("Pesquisando em: ", root)
    for diretorios in dirs:
        contadorDeDiretorios += 1
    for arquivos in files:
        contadorDeArquivos +=1 

#Resultado

print("Número de arquivos: ", contadorDeArquivos)
print("Número de diretorios: ", contadorDeDiretorios)
print("Total: ", (contadorDeDiretorios, contadorDeArquivos))

