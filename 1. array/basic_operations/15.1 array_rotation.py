
def rotate_left_once(nums: list[int]) -> list[int]:
    first_element: int = nums[0]
    n: int = len(nums)

    for i in range (n - 1):
        nums[i] = nums[i + 1]

    nums[n - 1] = first_element

    return nums

def rotate_right_once(nums: list[int]) -> list[int]:
    n: int = len(nums)
    end_element = nums[n - 1]

    for i in range (n - 1, 0, -1):
        nums[i] = nums[i - 1]

    nums[0] = end_element

    return nums

def rotate_left_k_times(nums: list[int], k: int) -> list[int]:
    n: int = len(nums)
    k: int = k % n

    return nums[k:] + nums[:k]

if __name__ == "__main__":

    origin_arr = [10, 20, 30, 40, 50]

    print("Mảng gốc:      ", origin_arr)
    print("Switch left once:", rotate_left_once(list(origin_arr)))  # [20, 30, 40, 50, 10]
    print("Switch right once:", rotate_right_once(list(origin_arr))) # [50, 10, 20, 30, 40]
    print("Switch left twice", rotate_left_k_times(list(origin_arr), 2)) # [30, 40, 50, 10, 20]