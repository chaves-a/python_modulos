# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

# Usando um caminho do meu computador que tenha imagens:
# /home/chaves-a/Imagens

# o primeiro for pega o primeiro nível e o segundo for pega o segundo nível, ou seja, o que está dentro da pasta

import os

caminho = os.path.join('/home', 'chaves-a', 'Imagens')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
