class Solution:
    def reverse(self, x: int) -> int:
        # lay số cuối
        # bỏ số cuối
        # ghép số mới
        result: int = 0
        while x != 0:
            digit: int = x % 10
            result: int = result * 10 + digit
            x = x // 10
        return result

if __name__ == "__main__":
    s: Solution = Solution()
    print(s.reverse(123))