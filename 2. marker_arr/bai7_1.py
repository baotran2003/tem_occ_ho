
"""
Bài 7: Tìm ký tự xuất hiện nhiều nhất
Yêu cầu: Cho một chuỗi ký tự chỉ bao gồm các chữ cái tiếng Anh viết thường (từ 'a' đến 'z'). Hãy tìm ký tự xuất hiện với tần suất nhiều nhất trong chuỗi và xác định số lần xuất hiện của ký tự đó.

Ví dụ: * Đầu vào (Input): "babbac"

Đầu ra (Output): Ký tự b xuất hiện 3 lần.


"""
from typing import Tuple, List

def find_most_frequent_char(s: str) -> Tuple[str, int]:
    freq_arr: List[int] = [0] * 26  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] -> [2, 3, 1, 0, ...]

    for char in s:
        index: int = ord(char) - ord('a')
        freq_arr[index] += 1

    max_count: int = 0
    max_char: str = ''

    for i in range (len(freq_arr)):
        if freq_arr[i] > max_count:
            max_count = freq_arr[i]
            max_char = chr(i + ord('a'))

    return max_char, max_count


if __name__ == "__main__":
    input_str = "babbac"
    char, count = find_most_frequent_char(input_str)
    print(f"The character '{char}' appears most often with {count} times.")
