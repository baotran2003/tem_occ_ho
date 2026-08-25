from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def getLength(self, head: Optional[ListNode]) -> int:
    #     count: int = 0
    #     current_node: Optional[ListNode] = head
    #
    #     while current_node:
    #         count += 1
    #         current_node = current_node.next
    #     return count
    #
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     length: int = self.getLength(head)
    #     middle_node: int = length // 2
    #     current_node: Optional[ListNode] = head
    #
    #     for _ in range(middle_node):
    #         current_node = current_node.next
    #
    #     return current_node

    # Cach 2: Fast and Slow

if __name__ == "__main__":
    sol = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)  # head trỏ tới node 1

    result_head: Optional[ListNode] = sol.middleNode(head)
    print("Danh sách sau khi xóa:")
    curr = result_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next