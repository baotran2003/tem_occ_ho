def sum(n: int) -> int:
    if n == 0:
        return 0

    result: int = n + sum(n - 1)
    return result


if __name__ == "__main__":
    print(sum(5))
