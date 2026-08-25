
def delete_element(nums: list[int], k: int) -> list[int]:
    # result_arr: list[int] = []
    # for num in nums:
    #     if num != k:
    #         result_arr.append(num)
    # return result_arr

    # tan dung :k va k: va dung con tro

    index_write: int = 0

    for i in range (len(nums)):
        if nums[i] != k :
            nums[index_write] = nums[i]
            index_write += 1

    del nums[index_write:]

    return nums


if __name__ == "__main__":
    numbers: list[int] = [1, 5 , 3, 17, 8, 22, 22]
    print("array after remove:", delete_element(numbers, 22))