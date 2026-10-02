from typing import List

# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return []

if __name__ == "__main__":
    so: Solution = Solution()
    numbers: List[int] = [2, 7, 11, 15]
    target: int = 9
    print(so.twoSum(numbers, target))