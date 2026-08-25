class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n: int = len(haystack)
        m: int = len(needle)

        # chi can duyet tu 0 -> n - m
        for i in range(0, n - m + 1):
            if haystack[i: i + m] == needle:
                return i

        return -1

if __name__ == "__main__":
    s: Solution = Solution()
    print(s.strStr("abcbutsad", "sad"))