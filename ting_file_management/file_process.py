import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    for i in range(len(instance)):
        file = instance.search(i)
        if file["nome_do_arquivo"] == path_file:
            return print("Arquivo já processado", file=sys.stderr)
    file_lines = txt_importer(path_file)
    item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    instance.enqueue(item)
    print(item, file=sys.stdout)


def remove(instance: Queue):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)
    try:
        removed_item = instance.dequeue()
        return print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )
    except IndexError as error:
        return print(error, file=sys.stderr)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
