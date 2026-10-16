"""
Đề bài: Tìm xem có 2 phần tử bằng nhau nums[i] == nums[j] sao cho khoảng cách abs(i - j) <= k hay không.
Cách tư duy: Kết hợp Sliding Window và cấu trúc dữ liệu set.
Duy trì một set chứa tối đa k phần tử gần nhất. Khi cửa sổ vượt quá k, xóa phần tử cũ nhất ở mép trái ra khỏi set.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Time complexity: O(n^2)
        # n: int = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):     for j in range(i + 1, min(i + k + 1, n))
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        # HashSet + Sliding Window
        # windows: set[int] = set()
        #
        # for i in range(len(nums)):
        #     if i > k:
        #         windows.remove(nums[i - k - 1])
        #
        #     if nums[i] in windows:
        #         return True
        #
        #     windows.add(nums[i])
        # return False

        # HashMap
        seen: dict[int, int] = {}   # value - index

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False




if __name__ == "__main__":
    so: Solution = Solution()
    nums: list[int] = [1,2,1,3]
    k: int = 2
    print(so.containsNearbyDuplicate(nums, k))