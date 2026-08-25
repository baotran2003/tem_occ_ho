

if __name__ == '__main__':
    n = 5
    for i in range(1, n + 1):
        print(" " * (n - i) + "# " * i)

    for i in range(1, n + 1):
        print((" " * (n - i)) + ("#" * i))