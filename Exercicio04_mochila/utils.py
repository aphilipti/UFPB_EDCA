def read_instance(path):

    with open(path, "r") as f:

        lines = [line.strip() for line in f if line.strip()]

    n, capacity = map(int, lines[0].split())

    weights = []
    values = []

    for line in lines[1:]:

        weight, value = map(int, line.split())

        weights.append(weight)
        values.append(value)

    return n, capacity, weights, values