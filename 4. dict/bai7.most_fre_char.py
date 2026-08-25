
"""
Bài 7: Tìm ký tự xuất hiện nhiều nhất
Yêu cầu: Cho một chuỗi ký tự chỉ bao gồm các chữ cái tiếng Anh viết thường (từ 'a' đến 'z'). Hãy tìm ký tự xuất hiện với tần suất nhiều nhất trong chuỗi và xác định số lần xuất hiện của ký tự đó.

Ví dụ: * Đầu vào (Input): "babbac"

Đầu ra (Output): Ký tự b xuất hiện 3 lần.
"""
from typing import Tuple, List

def find_most_frequent_char(s: str) -> Tuple[str, int]:
    # dem so lan xuat hien
    fre_map: dict[str, int] = {}

    for char in s:
        fre_map[char] = fre_map.get(char, 0) + 1

    max_char: str = ''
    max_count: int = 0

    for char, count in fre_map.items():
        if count > max_count:
            max_count = count
            max_char = char

    return max_char, max_count

if __name__ == "__main__":
    input_str = "babbac"
    char, count = find_most_frequent_char(input_str)
    print(f"The character '{char}' appears most often with {count} times.")
