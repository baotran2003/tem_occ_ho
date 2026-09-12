class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.helper(x, -n)
        else:
            return self.helper(x, n)

    def helper(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1

        if n % 2 != 0:
            return x * self.helper(x, n - 1)
        else:
            half: float = self.helper(x , n // 2)
            return half * half

if __name__ == "__main__":
    s: Solution = Solution()
    print(s.myPow(2, 4))


