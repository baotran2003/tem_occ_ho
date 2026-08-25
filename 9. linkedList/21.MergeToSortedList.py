from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy: ListNode = ListNode()
        current_node: ListNode = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2

        return dummy


def print_linked_list(head: Optional[ListNode]):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def main():
    # list1: 1 -> 2 -> 4
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node1.next = node2
    node2.next = node3

    print("List 1:      ", end="")
    print_linked_list(node1)

    # list2: 1 -> 3 -> 4
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    print("List 2:      ", end="")
    print_linked_list(node4)

    solution = Solution()

    # Truyền vào head của 2 linked list
    merged_head = solution.mergeTwoLists(node1, node4)

    # In kết quả
    print("Merge 2 Lists: ", end="")
    print_linked_list(merged_head)


if __name__ == "__main__":
    main()