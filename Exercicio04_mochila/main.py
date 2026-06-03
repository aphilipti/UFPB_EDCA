import os
import sys
import time

from utils import read_instance
from knapsack import knapsack


DATA_DIR = "data"
RESULT_FILE = "resultados.txt"


EXPECTED_RESULTS = {
    "mochila01.txt": 107,
    "mochila02.txt": 130
}


def get_all_files():

    return sorted([
        os.path.join(DATA_DIR, file)
        for file in os.listdir(DATA_DIR)
        if file.endswith(".txt")
    ])


def save_result(filename, value, items):

    with open(
        RESULT_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        items_text = ", ".join(
            map(str, items)
        )

        f.write(
            f"instância: {filename}\n"
        )

        f.write(
            f"valor : {value}\n"
        )

        f.write(
            f"produtos escolhidos : "
            f"{items_text}\n\n"
        )


def execute(file_path):

    n, capacity, weights, values = \
        read_instance(file_path)

    start = time.perf_counter()

    best_value, items = knapsack(
        weights,
        values,
        capacity
    )

    end = time.perf_counter()

    elapsed = end - start

    filename = os.path.basename(
        file_path
    )

    expected = EXPECTED_RESULTS.get(
        filename
    )

    print("=" * 50)
    print(f"Arquivo: {filename}")
    print(f"Itens: {n}")
    print(f"Capacidade: {capacity}")
    print()

    print(
        f"Valor máximo: "
        f"{best_value}"
    )

    print(
        f"Produtos escolhidos: "
        f"{items}"
    )

    if expected is not None:

        status = (
            "OK"
            if best_value == expected
            else "ERRO"
        )

        print(
            f"Resultado esperado: "
            f"{expected}"
        )

        print(
            f"Status: {status}"
        )

    print(
        f"Tempo: "
        f"{elapsed:.6f}s"
    )

    print("=" * 50)

    save_result(
        filename,
        best_value,
        items
    )


def clear_results():

    open(
        RESULT_FILE,
        "w",
        encoding="utf-8"
    ).close()

    print(
        "Arquivo resultados.txt limpo."
    )


def run_all():

    files = get_all_files()

    for file_path in files:

        execute(file_path)


def main():

    if len(sys.argv) < 2:

        print(
            "Uso:"
        )

        print(
            "python main.py "
            "data/mochila01.txt"
        )

        print(
            "python main.py all"
        )

        print(
            "python main.py clear"
        )

        return

    command = sys.argv[1]

    if command == "all":

        run_all()

    elif command == "clear":

        clear_results()

    else:

        execute(command)


if __name__ == "__main__":
    main()