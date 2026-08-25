"""
**Bài 8: Tìm số nguyên dương nhỏ nhất chưa xuất hiện**

**Yêu cầu:**
Cho một mảng gồm `n` phần tử số nguyên (có thể chứa cả số âm và số 0). Hãy tìm số nguyên dương nhỏ nhất (bắt đầu từ `1, 2, 3, ...`) không có mặt trong mảng đã cho.
**Ví dụ:**
* **Đầu vào (Input):** `[2, 3, -1, 1, 5]`
* **Đầu ra (Output):** `4`

**Giải thích:**
Các số nguyên dương `1`, `2`, `3` đã xuất hiện trong mảng, nên số nguyên dương nhỏ nhất còn thiếu là `4`.

### Gợi ý thuật toán
Một mảng có `n` phần tử thì số nguyên dương nhỏ nhất chưa xuất hiện chắc chắn sẽ nằm trong khoảng từ `1` đến `n + 1`.

Các bước thực hiện:
1. Tạo một mảng đánh dấu có kích thước `n + 1`, ban đầu tất cả các phần tử đều bằng `False`.

2. Duyệt qua mảng gốc:
   * Nếu phần tử có giá trị nằm trong khoảng từ `1` đến `n` thì đánh dấu vị trí tương ứng là `True`.

3. Duyệt lại mảng đánh dấu từ vị trí `1` đến `n`:
   * Vị trí đầu tiên có giá trị `False` chính là số nguyên dương nhỏ nhất chưa xuất hiện.

4. Nếu tất cả các vị trí từ `1` đến `n` đều đã được đánh dấu, kết quả là `n + 1`.
"""

def find_first_missing_positive (nums: list[int]) -> int:
    n: int = len(nums)
    max_nums: int = max(nums)
    marker_arr: list[int] = [0] * (max_nums + 1)

    for num in nums:
        marker_arr[num] = 1

    for i in range (1, len(marker_arr)):
        if marker_arr[i] == 0:
            return i
    return n + 1

if __name__ == "__main__":
    input_array = [2, 3, 1, 1, 5]       [0, 1, 1, 1, 0, 1]
    input_array_2 = [1, 2, 3,6, 4, 5]   [0, 1, 1, 1, 1, 1, 1]
    result = find_first_missing_positive(input_array)
    print(f"The smallest positive integer that has not yet appeared is: {result}")