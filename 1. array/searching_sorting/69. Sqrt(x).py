class Solution:
    def mySqrt(self, x: int) -> int:
        # i: int = 0
        # while i * i <= x:
        #     i += 1
        # return i - 1

        # binary search -> Time complexity: O(logx)
        if x <= 1:
            return x

        left: int = 0
        right: int = x // 2

        while left <= right:
            mid: int = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    s: Solution = Solution()
    print(s.mySqrt(8))