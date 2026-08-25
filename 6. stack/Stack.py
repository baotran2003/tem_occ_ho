class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Kiểm tra xem stack có rỗng không
        return len(self.items) == 0

    def push(self, item):
        # Thêm phần tử vào đỉnh (cuối list)
        self.items.append(item)
        print(f"Đã thêm '{item}' vào đỉnh Stack.")

    def pop(self):
        # Lấy và xóa phần tử ở đỉnh
        if not self.is_empty():
            return self.items.pop()
        return "Lỗi: Stack đang rỗng!"

    def peek(self):
        # Xem phần tử ở đỉnh mà không xóa
        if not self.is_empty():
            return self.items[-1]
        return "Lỗi: Stack đang rỗng!"

    def size(self):
        # Trả về số lượng phần tử
        return len(self.items)


if __name__ == "__main__":
    print("--- TEST STACK ---")
    my_stack = Stack()
    my_stack.push("Sách Toán")
    my_stack.push("Sách Lý")
    my_stack.push("Sách Hóa")

    print("Phần tử trên đỉnh hiện tại:", my_stack.peek())
    print("Lấy ra khỏi đỉnh:", my_stack.pop())
    print("Kích thước Stack hiện tại:", my_stack.size())