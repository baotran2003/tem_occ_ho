def build_prefix_sum(A: list[list[int]]) -> list[list[int]]:
    if not A or not A[0]:
        return []

    M: int = len(A)
    N: int = len(A[0])

    P: list[list[int]] = [[0] * (M +1) for _ in range (N + 1)]

    for i in range (1, N + 1):
        for j in range (1, M + 1):
            P[i][j] = A[i - 1][j - 1] + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]

    return P


def query_range_sum(P, x1, y1, x2, y2):
    return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]


if __name__ == "__main__":
    A = [
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [1, 4, 3, 2],
        [1, 1, 1, 1]
    ]

    print("---  PREFIX SUM P ")
    P = build_prefix_sum(A)

    for row in P:
        print("row: ", row)

    x1, y1 = 2, 2
    x2, y2 = 4, 4

    ans = query_range_sum(P, 2, 2, 4, 4)

    print(f"Sum of ({x1}, {y1}) -> ({x2}, {y2}) : {ans}")