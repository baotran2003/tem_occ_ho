from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        count: int = 0
        current_node: Optional[ListNode] = head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length: int = self.getLength(head)
        target_step: int = length - n

        dummy_node: ListNode = ListNode(-1, head)
        current_node: Optional[ListNode] = dummy_node

        for _ in range(target_step):
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

        return dummy_node.next


def main():
    sol = Solution()

    # Tạo các Node thủ công: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)  # head trỏ tới node 1

    n = 2  # Cần xóa nút thứ 2 từ cuối lên (nút giá trị 4)

    # Truyền head ListNode vào hàm và nhận về result_head ListNode
    result_head: Optional[ListNode] = sol.removeNthFromEnd(head, n)

    # In ra kết quả bằng cách duyệt ListNode
    print("Danh sách sau khi xóa:")
    curr = result_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next


if __name__ == "__main__":
    main()