class Solution:
    # O[ (n - k + 1) * (k logk) ]
    def findAnagrams_bruteforce(self, s: str, p: str) -> list[int]:
        # #brute force
        # n: int = len(s)
        # k: int = len(p)
        #
        # sorted_p: list[str] = sorted(p)
        # result: list[int] = []
        #
        # for i in range(n - k + 1):
        #     substring: str = s[i : i + k]
        #     if sorted_p == sorted(substring):
        #         result.append(i)
        #
        # return result

        # frequency count
        # n: int = len(s)
        # k: int = len(p)
        # result: list[int] = []
        #
        # freq_p: list[int] = [0] * 26
        # for ch in p:
        #     freq_p[ord(ch) - ord("a")] += 1
        #
        # for i in range(n - k + 1):
        #     window_count: list[int] = [0] * 26
        #     for j in range(i, i + k):
        #         window_count[ord(s[j]) - ord("a")] += 1
        #         if window_count == freq_p:
        #             result.append(i)
        #
        # return result

        n, k = len(s), len(p)
        if n < k:
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        result: list[int] = []

        # first window
        for i in range(k):
            p_count [ord(p[i]) - ord("a")] += 1
            s_count [ord(s[i]) - ord("a")] += 1

        if p_count == s_count:
            result.append(0)

        for i in range(k, n):
            # expand left
            s_count[ord(s[i]) - ord("a")] += 1
            # shirnk left
            s_count[ord(s[i - k]) - ord("a")] -= 1

            if s_count == p_count:
                result.append(i - k + 1)
        return result


if __name__ == "__main__":
    so: Solution = Solution()

    s: str = "aa"
    p: str = "bb"

    print(so.findAnagrams_bruteforce(s, p))