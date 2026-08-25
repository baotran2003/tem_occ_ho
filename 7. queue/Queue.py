from collections import deque

class Queue:
    def __init__(self):
        # Sử dụng deque thay vì list thông thường để tối ưu hiệu suất
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        # Thêm phần tử vào cuối hàng đợi
        self.items.append(item)
        print(f"'{item}' đã xếp vào hàng đợi.")

    def dequeue(self):
        # Lấy phần tử ở đầu hàng đợi ra (popleft)
        if not self.is_empty():
            return self.items.popleft()
        return "Lỗi: Queue đang rỗng!"

    def front(self):
        # Xem phần tử ở đầu hàng đợi
        if not self.is_empty():
            return self.items[0]
        return "Lỗi: Queue đang rỗng!"

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    print("\n--- TEST QUEUE ---")
    my_queue = Queue()
    my_queue.enqueue("Khách hàng A")
    my_queue.enqueue("Khách hàng B")
    my_queue.enqueue("Khách hàng C")

    print("Người đang chờ đầu tiên:", my_queue.front())
    print("Phục vụ và mời ra khỏi hàng:", my_queue.dequeue())
    print("Kích thước Queue hiện tại:", my_queue.size())