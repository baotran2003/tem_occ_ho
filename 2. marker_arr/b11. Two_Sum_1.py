
def find_pairs_with_sum_k(nums: list[int], target: int) -> list[list[int]]:
    max_val: int = max(nums)
    result_arr: list[list[int]] = []
    marker_arr: list[int] = [0] * (max_val + 1) #[0, 0, 0, 0, 0, 0] -> [1, 1, 1, 1, 0, 1] index_marker = num in nums

    for num in nums:
        complement: int = target - num
        if marker_arr[complement] == 1:
            result_arr.append([complement, num])        # complement = index marker_arr

        marker_arr[num] = 1

    return result_arr




if __name__ == "__main__":
    arr: list[int] = [0, 1, 2, 3, 5]
    k: int = 5
    print("Kết quả các cặp:", find_pairs_with_sum_k(arr, k))