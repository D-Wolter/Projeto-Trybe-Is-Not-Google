from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data_txt = txt_importer(path_file)
    data = {
        "nome_do_arquivo": f"{path_file}",
        "qtd_linhas": len(data_txt),
        "linhas_do_arquivo": data_txt,
    }
    if data in instance.queue:
        return None

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if (instance.__len__() == 0):
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
