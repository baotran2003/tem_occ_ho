"""
**Bài 9: Tìm giao của hai mảng số nguyên**

**Yêu cầu:**
Cho hai mảng số nguyên:

* Mảng `A` có kích thước `n`
* Mảng `B` có kích thước `m`

Hãy tìm và in ra các phần tử xuất hiện đồng thời ở cả hai mảng (phần giao).



**Đầu vào (Input):**

* `A = [1, 2, 2, 2, 3]`    [0, 1, 2, 1  các phần tu xuat hien trong cả a va b
* `B = [2, 2, 3, 4, 5]`     # So lan xuat hien x trong a la y,  2 -> 3
                            so lan xuat hien x trong b la z     2 -> 2 min (z, y
result_arr = [2, 2, 3]
marker_arr_1: [0, 1, 3, 1, 0, 0]
marker_arr_2: [0, 0, 2, 1, 1, 1]

add vao result_arr i x lần






**Đầu ra (Output):** 2 3

### Gợi ý thuật toán

**Bước 1:**
Tạo một mảng đánh dấu.
Duyệt qua toàn bộ các phần tử của mảng `A` và đánh dấu sự xuất hiện của chúng (ví dụ: gán giá trị bằng `1`).

**Bước 2:**
Duyệt qua từng phần tử của mảng `B`.
Nếu phần tử đang xét của `B` đã được đánh dấu là `1` từ mảng `A`, điều đó có nghĩa là phần tử này thuộc phần giao của hai mảng.

**Bước 3:**
In phần tử đó ra màn hình, đồng thời chuyển trạng thái đánh dấu tại vị trí đó thành một giá trị khác (ví dụ: gán bằng `2`).
Việc này giúp đảm bảo rằng nếu mảng `B` có các phần tử trùng lặp liên tiếp, chúng sẽ không bị in ra nhiều lần.
"""

def find_intersection_with_list(nums1: list[int], nums2: list[int]) -> list[int]:
    max_num: int = max(max(nums1), max(nums2))
    marker_arr: list[int] = [0] * (max_num + 1)
    result_arr: list[int] = []

    for num in nums1:
        marker_arr[num] = 1

    for num in nums2:
        if marker_arr[num] == 1:
            result_arr.append(num)
            marker_arr[num] = 0

    return result_arr

if __name__ == "__main__":
    A = [1, 2, 2, 3]
    B = [2, 2, 3, 5]

    print(find_intersection_with_list(A, B))
