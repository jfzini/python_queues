from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    lower_word = word.lower()
    matches = []
    for i in range(len(instance)):
        file = instance.search(i)
        data = {
            "palavra": lower_word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        lines = file["linhas_do_arquivo"]
        for li in range(len(lines)):
            if lower_word in lines[li].lower():
                data["ocorrencias"].append({"linha": li + 1})
        if len(data["ocorrencias"]) > 0:
            matches.append(data)
    return matches


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
