from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(caminho_projeto)
print(caminho_projeto.absolute())

camino_arquivo = Path(__file__)
print(camino_arquivo)

print(camino_arquivo.parent)
print(camino_arquivo.parent.parent)
print(camino_arquivo.parent.parent.parent)

# criando uma nova pasta dentro de python_modulos (apenas em memória)
ideias = camino_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

print(Path.home() / 'Documentos' / 'arquivo.txt')

# agora criando mesmo um arquivo

# arquivo = Path.home() / 'Documentos' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)

# escrevendo algo nele
# arquivo.write_text('Olá mundo')
# print(arquivo.read_text())

# apagando ele
# arquivo.unlink()

caminho_arquivo = Path.home() / 'Documentos' / 'arquivo.txt'

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(caminho_arquivo.read_text())
caminho_arquivo.unlink()

# criando pasta
caminho_pasta = Path.home() / 'Documentos' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    
    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('+a') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta)

def rmtree(root, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)