def giaiThua(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    result: int = n * giaiThua(n - 1)
    return result

if __name__ == "__main__":
    print(giaiThua(5))
