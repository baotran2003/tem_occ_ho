class Solution:
    def isPalindrome(self, s: str) -> bool:

        left: int = 0
        right: int = len(s) - 1

        s = s.lower()

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

        return True

if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "a'b''b'a"
    print(so.isPalindrome(s))