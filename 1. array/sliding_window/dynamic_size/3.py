"""
set: check exist + remove: O(1) + unique
expand right + shrink left
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: O(n^3)
    #     max_len: int = 0
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             if self.allUnique(s, i, j):
    #                 max_len = max(max_len, j - i)
    #     return max_len
    #
    #
    # def allUnique(self, s: str, start: int, end: int) -> bool:
    #     seen: set[str] = set()
    #
    #     for i in range(start, end):
    #         if s[i] in seen:
    #             return False
    #         seen.add(s[i])
    #     return True

        # O(n^2)
        max_len: int = 0

        for i in range(len(s)):
            seen: set[str] = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len

if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "aabebcc"
    print(so.lengthOfLongestSubstring(s))