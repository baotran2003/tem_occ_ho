from typing import List

def move_zeroes(nums: List[int]) -> List[int]:
    # result_arr: List[int] = []
    #
    # for num in nums:
    #     if num != 0:
    #         result_arr.append(num)
    #
    # count_zeroes: int = len(nums) - len(result_arr)
    # for _ in range(count_zeroes):
    #     result_arr.append(0)
    #
    # return result_arr

    #3 Use pointer
    # B1: tao 1 con tro k lam con tro ghi
    # B2: Duyet mang, neu gap phan tu != 0 lay nums[k] = nums[i] tang k len 1 don vi
    # B3 cho vong lap di tu k -> n va gan num[k] = 0

    k: int = 0
    n: int = len(nums)

    for i in range (n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    for i in range (k, n):
        nums[i] = 0

    return nums


if __name__ == "__main__":
    test_arr: List[int] = [0, 1, 0, 3, 12, 0, 5]
    print("Kết quả (Mảng mới):", move_zeroes(test_arr))