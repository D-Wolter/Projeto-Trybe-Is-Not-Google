def exists_word(word, instance):
    word_list = []
    for index in range(0, len(instance)):
        file = instance.search(index)
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for item, linha in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                data["ocorrencias"].append({"linha": item + 1})
        if data["ocorrencias"]:
            word_list.append(data)

    return word_list


def search_by_word(word, instance):
    word_list = []

    for file in instance.queue:
        occurrences = []
        for index, item in enumerate(file["linhas_do_arquivo"]):
            if word in item.lower():
                occurrences.append({"linha": index + 1, "conteudo": item})
        if len(occurrences):
            word_list.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return word_list
