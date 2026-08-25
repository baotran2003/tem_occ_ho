def isPerfectSquare(num: int) -> bool:
    # duyet chay
    i: int = 1

    while i * i <= num:
        if i * i == num:
            return True
        else:
            i += 1
    return False

    # left: int = 1
    # right: int = num
    #
    # while left <= right:
    #     mid: int = (left + right) // 2
    #     square: int = mid * mid
    #
    #     if square == num:
    #         return True
    #     elif square > num:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return False


if __name__ == "__main__":
    num: int = 16
    print(isPerfectSquare(num))