def permute(nums):
    result = []

    def backtrack(current, used):
        # Base case: khi danh sách hiện tại gom đủ số phần tử
        if len(current) == len(nums):
            result.append(current.copy())  # Lưu một bản sao của current
            return

        for i in range(len(nums)):
            if not used[i]:
                # 1. CHOOSE: Chọn phần tử nums[i]
                current.append(nums[i])
                used[i] = True

                # 2. EXPLORE: Đi tiếp vào nhánh đệ quy
                backtrack(current, used)

                # 3. UNCHOOSE (BACKTRACK): Hoàn tác lựa chọn để thử trường hợp khác
                current.pop()
                used[i] = False

    # Khởi tạo: danh sách rỗng và mảng đánh dấu chưa dùng
    backtrack([], [False] * len(nums))
    return result

if __name__ == "__main__":

    # Chạy thử với nums = [1, 2, 3]
    print(permute([1, 2, 3]))