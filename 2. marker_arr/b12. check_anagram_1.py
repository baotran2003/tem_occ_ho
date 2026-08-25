"""
Bài 2: Kiểm tra Chuỗi Đảo Nghịch (Anagram)

Đề bài:
Cho hai chuỗi ký tự S và T, chỉ gồm các chữ cái viết thường từ 'a' đến 'z'.

Hãy kiểm tra xem chuỗi T có phải là một hoán vị (anagram) của chuỗi S hay không.

Hai chuỗi được coi là anagram nếu:

Có cùng độ dài.
Chứa chính xác cùng các ký tự với cùng số lần xuất hiện.
Thứ tự các ký tự có thể khác nhau.

Nếu T là anagram của S, in ra YES; ngược lại, in ra NO.

Giới hạn:

1 ≤ |S|, |T| ≤ 10^5

"""

def anagram(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        return "NO"

    marker_arr: list[int] = [0] * 26

    for char1 in s1:
        index: int = ord(char1) - ord('a')
        marker_arr[index] += 1

    for char2 in s2:
        index: int = ord(char2) - ord('a')
        marker_arr[index] -= 1

    for num in marker_arr:
        if num != 0:
            return "NO"

    return "YES"

if __name__ == "__main__":
    S: str = "anagram"
    T: str = "nagaram"

    print("Output: ", anagram(S, T))