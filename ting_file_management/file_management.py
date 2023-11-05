import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            return print("Formato inválido", file=sys.stderr)
        with open(path_file, "r") as file:
            read_file = file.read()
            splited_file = read_file.split("\n")
            return splited_file
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
