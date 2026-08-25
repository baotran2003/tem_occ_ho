from typing import Optional
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

    @staticmethod
    def reverseList(head: Optional["Node"]) -> Optional[Node]:
        # current_node: Optional["Node"] = head
        # new_head: Optional["Node"] = None
        #
        # while current_node:
        #     new_node: Optional["Node"] = Node(current_node.data)
        #     new_node.next = new_head
        #
        #     new_head = new_node
        #
        #     current_node = current_node.next

        prev_node: Optional["Node"] = None
        current_node: Optional["Node"] = head

        while current_node:
            next_node: Optional["Node"] = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node