
def find_pairs_with_sum_k(nums: list[int], k: int) -> list[list[int]]:
    max_val: int = max(nums)
    marker_arr: list[int] = [False] * (max_val + 1)     #[False, False, False, False, False]
    result_arr: list[list[int]] = []

    for num in nums:
        target: int = k - num
        if 0 <= target <= max_val and marker_arr[target] == True:
            result_arr.append([target, num])

        marker_arr[num] = True

    return result_arr




if __name__ == "__main__":
    arr: list[int] = [0, 1, 2, 3, 5]
    k: int = 5
    print("Kết quả các cặp:", find_pairs_with_sum_k(arr, k))