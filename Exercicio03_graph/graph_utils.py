def read_graph(path):

    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])

    matrix = [[0] * n for _ in range(n)]

    row = 0

    for line in lines[1:]:

        values = list(map(int, line.split()))

        col = row + 1

        for value in values:

            matrix[row][col] = value
            matrix[col][row] = value

            col += 1

        row += 1

    return matrix