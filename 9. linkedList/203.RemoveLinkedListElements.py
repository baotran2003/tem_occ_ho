# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # while head and  head.val == val:
        #     head = head.next
        #
        # if head is None:
        #     return None
        #
        # prev_node = head
        # current_node = head.next
        #
        # while current_node:
        #     if current_node.val == val:
        #         prev_node.next = current_node.next
        #         current_node = current_node.next
        #     else:
        #         prev_node = current_node
        #         current_node = current_node.next
        # return head

        # Cach 1 tao ra node moi -> Time complexity: O(n)   Space complexity: O(n)

        # dummy: Optional[ListNode] = ListNode(0)     # diem bat dau cua node moi
        # current_new: Optional[ListNode] = dummy     # pointer cua node moi
        #
        # current_node: Optional[ListNode] = head
        #
        # while current_node:
        #     if current_node.val != val:
        #         current_new.next = ListNode(current_node.val)
        #         current_new = current_new.next
        #     current_node = current_node.next
        # return dummy.next

        # cach 2: ko can tao node moi
        dummy_node: Optional[ListNode] = ListNode(-1, head)
        # dummy_node.next = head      # gia su target dau tien tai vi tri head => can co dummy de luu lai, return ve vi tri do

        prev_node: Optional[ListNode] = dummy_node
        current_node: Optional[ListNode] = head
        v: set[ListNode] = set()

        while current_node:
            if current_node.val == val:
                prev_node.next = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next
        return dummy_node.next



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
    node5 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("List 1:      ", end="")
    print_linked_list(node1)

    solution: Solution = Solution()

    node1 = solution.removeElements(node1, 1)
    print("Merge 2 Lists: ", end="")
    print_linked_list(node1)


if __name__ == "__main__":
    main()