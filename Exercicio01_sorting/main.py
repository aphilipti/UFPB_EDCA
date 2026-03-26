import sys
import time
import os
from selection_sort import selection_sort
from insertion_sort import insertion_sort


DATA_DIR = "data"
LOG_FILE = "resultados.txt"


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split()

    n = int(lines[0])
    data = list(map(int, lines[1:]))

    if len(data) != n:
        print(f"Aviso em {path}: tamanho inconsistente")

    return data


def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("arquivo | algoritmo | tempo\n")
            f.write("--------------------------------\n")


def clear_log():
    with open(LOG_FILE, "w") as f:
        f.write("arquivo | algoritmo | tempo\n")
        f.write("--------------------------------\n")
    print("Log limpo com sucesso!")


def log_result(file_name, algorithm, execution_time):
    with open(LOG_FILE, "a") as f:
        f.write(f"{file_name} | {algorithm} | {execution_time:.6f}\n")


def run_algorithm(data, algorithm):
    if algorithm == "selection":
        return selection_sort(data.copy())
    elif algorithm == "insertion":
        return insertion_sort(data.copy())
    else:
        return None


def execute(file_path, algorithm):
    data = read_file(file_path)

    print(f"\nArquivo: {file_path}")
    print(f"Tamanho: {len(data)} | Algoritmo: {algorithm}")

    start = time.time()
    result = run_algorithm(data, algorithm)
    end = time.time()

    if result is None:
        print("Algoritmo inválido")
        return

    execution_time = end - start

    print(f"Tempo: {execution_time:.6f} segundos")
    print("Primeiros 10:", result[:10])

    file_name = os.path.basename(file_path)
    log_result(file_name, algorithm, execution_time)


def get_all_files():
    return [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".in")]


def run_all():
    files = get_all_files()
    for file in files:
        execute(file, "selection")
        execute(file, "insertion")


def run_all_selection():
    files = get_all_files()
    for file in files:
        execute(file, "selection")


def run_all_insertion():
    files = get_all_files()
    for file in files:
        execute(file, "insertion")


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print(" python main.py <arquivo> <algoritmo>")
        print(" python main.py all")
        print(" python main.py selection_all")
        print(" python main.py insertion_all")
        print(" python main.py clear")
        return

    init_log()

    command = sys.argv[1]

    if command == "clear":
        clear_log()
        return

    elif command == "all":
        run_all()
        return

    elif command == "selection_all":
        run_all_selection()
        return

    elif command == "insertion_all":
        run_all_insertion()
        return

    elif len(sys.argv) >= 3:
        file_path = sys.argv[1]
        algorithm = sys.argv[2]
        execute(file_path, algorithm)
        return

    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()