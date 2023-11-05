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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


new_queue = Queue()
new_queue2 = Queue()
# process("ting_file_management/example.txt", new_queue)
process("ting_file_management/example.txt", new_queue2)
process("ting_file_management/example.txt", new_queue2)
