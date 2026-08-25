def compareTriplets(a, b):
    point_a: int = 0
    point_b: int = 0

    for i in range (len(a)):
        if a[i] > b[i]:
            point_a += 1
        elif a[i] < b[i]:
            point_b += 1

    return [point_a, point_b]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = compareTriplets(a, b)

    print(*result)
