"""
set: check exist + remove: O(1) + unique
expand right + shrink left
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left: int = 0
        right: int = 0
        result: int = 0
        window: set[str] = set()

        while right < len(s):
            current: str = s[right]

            while current in window:
                window.remove(s[left])
                left += 1

            window.add(current)

            result = min(result, right - left + 1)

            right+= 1

        return result

if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "abcabcbb"
    print(so.lengthOfLongestSubstring(s))