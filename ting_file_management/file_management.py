import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write('Formato inválido')
    try:
        with open(path_file, "r") as data:
            content = data.read()
            return content.split('\n')
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
