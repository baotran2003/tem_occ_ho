

def print_unique(nums: list[int]) -> list[int]:
    # result_arr: list[int] = []
    #
    # for num in nums:
    #     if nums.count(num) == 1:
    #         result_arr.append(num)
    #
    # return result_arr

    # cach 2 dung dict  key-value
    frequency_map: dict[int, int] = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1     # value tang 1
        else :
            frequency_map[num] = 1      # neu chua co gan value cho num = 1

    result_arr: list[int] = []

    for num in frequency_map:
        if frequency_map[num] == 1:
            result_arr.append(num)

    return result_arr


if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 5, 3, 17, 8, 22, 22]

    print("unique_element:", print_unique(numbers)) # [1, 3, 17, 8]