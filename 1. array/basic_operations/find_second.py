from typing import List


def find_max_with_index(nums: List[int]) -> List[int]:
    max_num: int = nums[0]
    index: int = 0

    for i in range (len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            index = i
    return [max_num, index]

if __name__ == "__main__":
    numbers: list[int] = [1, 4, 2, 6, 10, 10, 12, 12]  #[12, 6]
    result: List[int] = find_max_with_index(numbers)

    print("The second_largest number is:", result)
