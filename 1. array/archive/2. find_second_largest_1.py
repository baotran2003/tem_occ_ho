from typing import List, Optional

def second_distinct_max(nums):
    max_num = float('-inf')
    second_max = float('-inf')

    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num

        elif max_num > num > second_max:
            second_max = num

        # truong hop nho hon ko can lam gi

    return second_max

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10, 12]
    result: int = second_distinct_max(numbers)

    print("The second_largest number is:", result)


