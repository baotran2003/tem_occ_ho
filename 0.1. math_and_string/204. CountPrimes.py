from typing import List

class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1: return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        # count: int = 0
        # x_prime = 2
        # while x_prime < n:
        #     if self.isPrime(x_prime):
        #         count += 1
        #     x_prime += 1
        # return count

        is_prime: List[int] = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        for i in range (2, int(n ** 0.5) + 1):
            for j in range(i * i, n, i):
                is_prime[j] = False

        count: int = 0
        for i in range(len(is_prime)):
            if is_prime[i]:
                count += 1
        return count


if __name__ == "__main__":
    s: Solution = Solution()
    print(s.countPrimes(100))