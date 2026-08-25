def build_prefix_sum(A: list[list[int]]) -> list[list[int]]:
    if not A or not A[0]:
        return []

    cols: int = len(A)
    rows: int = len(A[0])

    P: list[list[int]] = [[0] * (cols + 1) for _ in range (rows + 1)]

    for r in range (1, rows + 1):
        for c in range (1, cols + 1):
            P[r][c] = P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1] + A[r - 1][c - 1]

    return P

def query_range_sum (P, x1, y1, x2, y2) -> list[list[int]]:
    return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]


if __name__ == "__main__":
    A = [
        [1, 1, 1, 1],               # [1, 2, 3, 4]
        [1, 2, 3, 4],               # [0, 2, 3, 4],
        [1, 4, 3, 2],       # ->    # [0, 4, 3, 2],
        [1, 1, 1, 1]                # [0, 1, 1, 1]
    ]

    print("---  PREFIX SUM P ")
    P = build_prefix_sum(A)

    for row in P:
        print("row: ", row)

    x1, y1 = 2, 2
    x2, y2 = 4, 4

    ans = query_range_sum(P, 2, 2, 4, 4)

    print(f"Sum of ({x1}, {y1}) -> ({x2}, {y2}) : {ans}")