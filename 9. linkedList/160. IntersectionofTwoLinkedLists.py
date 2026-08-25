from typing import Optional

class ListNode:
    def __init__(self, x: int = 0):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visit_node: set[ListNode] = set()

        current_A: Optional[ListNode] = headA
        while current_A:
            visit_node.add(current_A)
            current_A = current_A.next

        current_B: Optional[ListNode] = headB
        while current_B:
            if current_B in visit_node:
                return current_B

            current_B = current_B.next
        return None


if __name__ == "__main__":
    # -------------------------------------------------------------
    # CASE 1: Hai danh sách GIAO NHAU tại node có giá trị là 8
    #
    # Danh sách A: 4 -> 1 \
    #                      8 -> 4 -> 5  (Đoạn chung)
    # Danh sách B: 5 -> 6 -> 1 /
    # -------------------------------------------------------------

    # 1. Tạo các node thuộc đoạn chung
    common_8 = ListNode(8)
    common_4 = ListNode(4)
    common_5 = ListNode(5)

    # Nối đoạn chung: 8 -> 4 -> 5 -> None
    common_8.next = common_4
    common_4.next = common_5

    # 2. Tạo danh sách A riêng: 4 -> 1
    headA = ListNode(4)
    a_1 = ListNode(1)
    headA.next = a_1
    a_1.next = common_8  # Nối đuôi A vào node giao điểm (8)

    # 3. Tạo danh sách B riêng: 5 -> 6 -> 1
    headB = ListNode(5)
    b_6 = ListNode(6)
    b_1 = ListNode(1)
    headB.next = b_6
    b_6.next = b_1
    b_1.next = common_8  # Nối đuôi B vào node giao điểm (8)

    # 4. Kiểm tra hàm
    solution = Solution()
    intersection = solution.getIntersectionNode(headA, headB)

    print("--- Test Case 1 ---")
    if intersection:
        print(f"Giao điểm tìm thấy có giá trị là: {intersection.val}")
    else:
        print("Không có giao điểm!")