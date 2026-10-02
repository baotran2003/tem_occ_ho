class Solution:
    def reverse_str(self, s: list[str]) -> str:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

if __name__ == "__main__":
    so: Solution = Solution()
    s: list[str] = ["h","e","l","l","o"]
    print(so.reverse_str(s))