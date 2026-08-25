from typing import List


def find_max_with_index(nums: List[int]) -> List[int]:
    max_sum = nums[0]
    min_sum: int = nums[0]
    second_max: int = nums[0]
    third_max: int = nums[0]


    index: int = 0
    index1: int = 0
    index2: int = 0

    for i in range(len(nums)):
        if nums[i] > max_sum:
            max_sum = nums[i]
            index = i

        if nums[i] <= min_sum:
            min_sum = nums[i]
            index1 = i

    for i in range (len(nums)):
        if nums[i] > second_max and i != index:
            second_max = nums[i]
            index1 = i
    for i in range (len(nums)):
        if nums[i] > third_max and i != index1 and i != index :
            third_max = nums[i]
            index2 = i


    return [third_max, index2]



if __name__ == "__main__":
    numbers: list[int] = [1, 1, 1, 4, 2, 6, 10, 10,12, 12]  #[12, 6]
    result: List[int] = find_max_with_index(numbers)

    print("The second_largest number is:", result)
