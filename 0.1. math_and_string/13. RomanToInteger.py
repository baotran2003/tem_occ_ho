class Solution:
    def romanToInt(self, s: str) -> int:
        rn: dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        n: int = len(s)
        total: int = 0
        prev: int = 0
        for i in range(n - 1, -1, -1):
            current: int = rn[s[i]]
            if current >= prev:
                total += current
                prev = current
            else:
                total -= current
                prev = current

        return total

def main():
    solution = Solution()

    s = input("Nhập số La Mã: ").strip().upper()

    result = solution.romanToInt(s)
    print(f"Giá trị số nguyên: {result}")


if __name__ == "__main__":
    main()
