"""
set: check exist + remove: O(1) + unique
expand right + shrink left
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left: int = 0
        right: int = 0
        result: int = 0
        window: List[str] = []

        while right < len(s):
            current: str = s[right]

            if current not in window:
                # mo rong window tu right
                window.append(current)
                right += 1
                result = max(right - left, result)  # right - left: len(window hien tai)
            else:
                # thu nho window tu left
                window.remove(s[left])
                left += 1
                s1: str = s[left]


        return result

if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "aabebcc"
    print(so.lengthOfLongestSubstring(s))