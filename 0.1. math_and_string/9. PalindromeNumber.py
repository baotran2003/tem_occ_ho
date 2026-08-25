class Solution:
    def isPalindrome(self, x: int) -> bool:
        s: str = str(x)
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -=1
        return True

if __name__ == "__main__":
    s: Solution = Solution()
    print(s.isPalindrome(121))