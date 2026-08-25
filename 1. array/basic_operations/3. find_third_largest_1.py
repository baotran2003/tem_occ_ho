from typing import List, Optional

def third_distinct_max(nums):
    max_num = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')


    for num in nums:
        if num > max_num:
            third_max = second_max
            second_max = max_num
            max_num = num

        elif max_num > num > second_max > third_max:
            third_max = second_max
            second_max = num
        elif second_max > num > third_max:
            third_max = num

        # truong hop nho hon ko can lam gi

    return third_max

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10, 12]
    result: int = third_distinct_max(numbers)

    print("The second_largest number is:", result)


