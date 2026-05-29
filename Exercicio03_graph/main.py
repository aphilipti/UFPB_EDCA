import os
import sys
import time

from graph_utils import read_graph
from prim import prim
from kruskal import kruskal
from dijkstra import dijkstra


DATA_DIR = "data"
RESULT_FILE = "resultados.txt"


EXPECTED_RESULTS = {

    "mst": {
        "dij10.txt": 7072,
        "dij20.txt": 15238,
        "dij40.txt": 26615,
        "dij50.txt": 30424,
    },

    "dijkstra": {
        "dij10.txt": 5183,
        "dij20.txt": 3190,
        "dij40.txt": 8928,
        "dij50.txt": 6764,
    }
}


def get_all_files():

    return sorted([
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if f.endswith(".txt")
    ])


def run_algorithm(graph, algorithm):

    if algorithm == "prim":
        return prim(graph)

    elif algorithm == "kruskal":
        return kruskal(graph)

    elif algorithm == "dijkstra":
        return dijkstra(graph)

    else:
        raise ValueError("Algoritmo inválido")


def get_expected(filename, algorithm):

    if algorithm in ["prim", "kruskal"]:
        return EXPECTED_RESULTS["mst"][filename]

    return EXPECTED_RESULTS["dijkstra"][filename]


def save_result(filename, algorithm, result, expected, status, elapsed):

    with open(RESULT_FILE, "a") as f:

        f.write(
            f"{filename} | "
            f"{algorithm} | "
            f"{result} | "
            f"{expected} | "
            f"{status} | "
            f"{elapsed:.6f}\n"
        )


def execute(file_path, algorithm):

    graph = read_graph(file_path)

    filename = os.path.basename(file_path)

    start = time.perf_counter()

    result = run_algorithm(graph, algorithm)

    end = time.perf_counter()

    elapsed = end - start

    expected = get_expected(filename, algorithm)

    status = "OK" if result == expected else "ERRO"

    print("=" * 50)
    print(f"Arquivo: {filename}")
    print(f"Algoritmo: {algorithm}")
    print()
    print(f"Resultado obtido: {result}")
    print(f"Resultado esperado: {expected}")
    print(f"Status: {status}")
    print(f"Tempo: {elapsed:.6f}s")
    print("=" * 50)

    save_result(
        filename,
        algorithm,
        result,
        expected,
        status,
        elapsed
    )


def clear_results():

    open(RESULT_FILE, "w").close()

    print("Arquivo resultados.txt limpo.")


def run_all():

    algorithms = ["prim", "kruskal", "dijkstra"]

    for file_path in get_all_files():

        for algorithm in algorithms:
            execute(file_path, algorithm)


def run_algorithm_all(algorithm):

    for file_path in get_all_files():
        execute(file_path, algorithm)


def main():

    if len(sys.argv) < 2:

        print("Uso:")
        print("python main.py all")
        print("python main.py prim_all")
        print("python main.py kruskal_all")
        print("python main.py dijkstra_all")
        print("python main.py clear")
        print("python main.py data/dij10.txt prim")

        return

    command = sys.argv[1]

    if command == "clear":

        clear_results()

    elif command == "all":

        run_all()

    elif command == "prim_all":

        run_algorithm_all("prim")

    elif command == "kruskal_all":

        run_algorithm_all("kruskal")

    elif command == "dijkstra_all":

        run_algorithm_all("dijkstra")

    else:

        if len(sys.argv) != 3:
            print("Uso inválido")
            return

        file_path = sys.argv[1]
        algorithm = sys.argv[2]

        execute(file_path, algorithm)


if __name__ == "__main__":
    main()