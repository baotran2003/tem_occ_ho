class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        # 1. Bỏ qua khoảng trắng ở cuối chuỗi
        while i >= 0 and s[i] == ' ':
            i -= 1

        # 2. Đếm độ dài của từ cuối cùng
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length