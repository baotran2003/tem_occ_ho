# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current_node: Optional["ListNode"] = head

        while current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head

def print_linked_list(head: Optional[ListNode]):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def main():
    # list1: 1 -> 2 -> 4
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(4)
    node4 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("List 1:      ", end="")
    print_linked_list(node1)

    solution: Solution = Solution()

    solution.deleteDuplicates(node1)
    print("Merge 2 Lists: ", end="")
    print_linked_list(node1)


if __name__ == "__main__":
    main()