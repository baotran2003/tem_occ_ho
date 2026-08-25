
"""
Bài 7: Tìm ký tự xuất hiện nhiều nhất
Yêu cầu: Cho một chuỗi ký tự chỉ bao gồm các chữ cái tiếng Anh viết thường (từ 'a' đến 'z'). Hãy tìm ký tự xuất hiện với tần suất nhiều nhất trong chuỗi và xác định số lần xuất hiện của ký tự đó.

Ví dụ: * Đầu vào (Input): "babbac"

Đầu ra (Output): Ký tự b xuất hiện 3 lần.

Gợi ý thuật toán: Bản chất của các ký tự trong máy tính được biểu diễn bằng mã ASCII (là các số nguyên).
Bạn có thể tận dụng điều này để tạo một mảng đánh dấu (mảng tần suất) gồm 26 phần tử, tương ứng với 26 chữ cái từ 'a' đến 'z'.

Khi duyệt qua một ký tự c, vị trí chỉ số (index) tương ứng trong mảng đánh dấu sẽ được tính bằng công thức: c - 'a'.

Tăng giá trị tại vị trí đó lên 1 đơn vị. Cuối cùng, tìm vị trí có giá trị lớn nhất trong mảng.
"""
from typing import Tuple, List

def find_most_frequent_char(s: str) -> Tuple[str, int]:
    count_arr: List[int] = [0] * 26

    for char in s:
        index: int = ord(char) - ord('a')
        count_arr[index] += 1

    max_count = 0
    max_char = ''

    for i in range (26):
        if count_arr[i] > max_count:
            max_count = count_arr[i]
            max_char = chr(i + ord('a'))

    return max_char, max_count

if __name__ == "__main__":
    input_str = "babbac"
    char, count = find_most_frequent_char(input_str)
    print(f"The character '{char}' appears most often with {count} times.")
