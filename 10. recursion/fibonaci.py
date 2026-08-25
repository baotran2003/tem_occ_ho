def fibonaci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

if __name__ == "__main__":
    print(fibonaci(7))