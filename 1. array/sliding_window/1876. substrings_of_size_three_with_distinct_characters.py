class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # count = 0
        # for i in range(len(s) - 2):
        #     a, b, c = s[i], s[i + 1], s[i + 2]
        #     if a != b and b != c and a != c:
        #         count += 1
        # return count

        count = 0
        left = 0

        for right in range(len(s)):
            # Khi cửa sổ đủ kích thước 3 (right - left + 1 == 3)
            if right - left + 1 == 3:
                # Kiểm tra 3 ký tự từ left đến right
                if s[left] != s[left + 1] and s[left + 1] != s[right] and s[left] != s[right]:
                    count += 1
                left += 1  # Trượt mép trái sang phải

        return count


if __name__ == "__main__":
    so: Solution = Solution()
    s: str = "xyzzaz"
    print(so.countGoodSubstrings(s))