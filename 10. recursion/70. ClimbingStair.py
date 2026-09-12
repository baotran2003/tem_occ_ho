class Solution:
    def climbStairs(self, n: int) -> int:
        memo: dict[int, int] = {}

        def helper(n):
            # base case
            if n <= 1:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = helper(n - 1) + helper(n - 2)
            return memo[n]

        return helper(n)

if __name__ == "__main__":
    s: Solution = Solution()
    result = s.climbStairs(4)
    print(result)