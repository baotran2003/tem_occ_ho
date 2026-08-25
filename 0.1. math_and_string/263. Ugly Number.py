class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            flag: bool = False
            # hoac tao ra bien old = n. Neu sau khi chay qua tat ca dieu kien ma n ko thay doi <=> n == odd -> return False

            if n % 2 == 0:
                n = n // 2
                flag = True

            if n % 3 == 0:
                n = n // 3
                flag = True

            if n % 5 == 0:
                n = n // 5
                flag = True

            if not flag:
                return False

        return True

if __name__ == "__main__":
    s: Solution = Solution()
    print("Is Ugly: ", s.isUgly(11))