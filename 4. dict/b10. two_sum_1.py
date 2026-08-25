if __name__ == "__main__":
    arr: list[int] = [0, 1, 2, 3, 5]
    k: int = 5

    result_arr: list[list[int]] = []

    # Khởi tạo dict để lưu: Key là GIÁ TRỊ số, Value là CHỈ SỐ (INDEX) của số đó
    seen_dict: dict[int, int] = {}

    for j in range(len(arr)):
        current_num = arr[j]
        complement = k - current_num

        # Kiểm tra xem số bù (complement) đã từng xuất hiện trước đó chưa
        if complement in seen_dict:
            # Nếu có, lấy index của số bù ra là seen_dict[complement]
            i = seen_dict[complement]
            result_arr.append([i, j])

        # Lưu số hiện tại và vị trí của nó vào dict để các số đứng sau đối chiếu
        seen_dict[current_num] = j

    print(result_arr)  # Output: [[0, 4], [2, 3]]