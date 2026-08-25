from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    n: int = len(nums)
    total_pair: int = 0
    # count: int = 0
    #
    # for i in range (n):
    #     for j in range(i + 1, n):
    #         if nums[i] == nums[j]:
    #             count += 1
    # return count

    #c2: dung cong thuc: so cap trung nhau V x (V - 1) / 2
    # freq_map: dict[int, int] = {}
    # for num in nums:
    #     freq_map[num] = freq_map.get(num, 0) + 1
    #
    # for count in freq_map.values():
    #     total_pair += (count * (count - 1)) // 2
    #
    # return total_pair

    freq_map: dict[int, int] = {}
    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            total_pair += freq_map[num]
            freq_map[num] += 1
    return total_pair

if __name__ == "__main__":
    nums1: List[int] = [1,2,3,1,1,3]
    print("output: ", numIdenticalPairs(nums1))

    # nums2: List[int] = [1, 1, 1, 1]
    # print("output: ", numIdenticalPairs(nums2))
    #
    # nums3: List[int] = [1, 2, 3]
    # print("output: ", numIdenticalPairs(nums3))