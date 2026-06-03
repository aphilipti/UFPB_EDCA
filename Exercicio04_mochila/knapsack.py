def knapsack(weights, values, capacity):

    n = len(weights)

    dp = [0] * (capacity + 1)

    keep = [[False] * (capacity + 1)
            for _ in range(n)]

    for i in range(n):

        weight = weights[i]
        value = values[i]

        for w in range(capacity, weight - 1, -1):

            candidate = dp[w - weight] + value

            if candidate > dp[w]:

                dp[w] = candidate
                keep[i][w] = True

    selected_items = []

    w = capacity

    for i in range(n - 1, -1, -1):

        if keep[i][w]:

            selected_items.append(i + 1)
            w -= weights[i]

    selected_items.reverse()

    return dp[capacity], selected_items