def getRow(rowIndex: int) -> list[int]:
    # current_row: list[int] = [1]
    #
    # for _ in range (1, rowIndex + 1):
    #     new_row: list[int] = [1] * (len(current_row) + 1)
    #
    #     for i in range(1, len(new_row) - 1):
    #         new_row[i] = current_row[i - 1] + new_row[i]
    #
    #     current_row = new_row
    # return current_row

    # RECURSION
    # if rowIndex == 0:
    #     return [1]
    #
    # prev_row: list[int] = getRow(rowIndex - 1)
    # current_row: list[int] = [1] * (len(prev_row) + 1)
    #
    # for i in range(1, len(current_row) - 1):
    #     current_row[i] = prev_row[i - 1] + prev_row[i]
    #
    # return current_row

    # In-place với 1 mảng duy nhất cach 1
    # row: list[int] = [1] * (rowIndex + 1)
    #
    # # update tu dong 2 -> rowIndex. Vi dong 0 va 1 la so "1"
    # for i in range (2, rowIndex + 1):
    #     for j in range(i - 1, 0, -1):
    #         row[j] = row[j] + row[j - 1]
    # return row

    row: list[int] = [1]

    for i in range (1, rowIndex + 1):
        row.append(1)

        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    return row

def main():
    # 1. Chạy thử một vài trường hợp mẫu
    test_cases = [0, 1, 3, 4]
    print("--- Kết quả các trường hợp mẫu ---")
    for row in test_cases:
        print(f"rowIndex = {row} -> {getRow(row)}")

    # 2. Nhập dữ liệu trực tiếp từ bàn phím
    print("\n--- Tự nhập giá trị để test ---")
    try:
        user_input = int(input("Nhập rowIndex: "))
        if user_input < 0:
            print("Vui lòng nhập số nguyên không âm (>= 0).")
        else:
            result = getRow(user_input)
            print(f"Dòng {user_input} của tam giác Pascal là: {result}")
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào phải là số nguyên!")


if __name__ == "__main__":
    main()