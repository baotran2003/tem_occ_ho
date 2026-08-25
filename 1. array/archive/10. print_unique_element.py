from typing import List, Dict

def print_unique(nums: list[int]) -> List[int]:
    # Cach 1: use .count()

    # Cach 2: dict{key - value}
    frequency_map: Dict[int, int] = {}

    # review array + count the number of occurrences
    for num in nums:                #[1, 2, 2, 5]
        if num in frequency_map:
            frequency_map[num] += 1
        else:                       #key: value = [ 1: 1, 2: 1, 5: 2]
            frequency_map[num] = 1
    # complete for: key-value = {1: 1, 2: 2, 5: 1}
    result_arr: List[int] = []
    for num in frequency_map:
        if frequency_map[num] == 1:
            result_arr.append(num)
    return result_arr


if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 5, 3, 17, 8, 22, 22]

    print("unique_element:", print_unique(numbers))