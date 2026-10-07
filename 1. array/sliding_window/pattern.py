left = 0
result = 0

for right in range(len(nums)):
    # 1. Thêm nums[right] vào trạng thái cửa sổ (state/dict/sum)
    # ...

    # 2. Khi điều kiện bị vi phạm, dùng while để co left
    while window_is_invalid:
        # Loại bỏ nums[left] khỏi trạng thái cửa sổ
        # ...
        left += 1

    # 3. Cập nhật kết quả với cửa sổ hợp lệ [left, right]
    result = max(result, right - left + 1)