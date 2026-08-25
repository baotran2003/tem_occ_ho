from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit_node: set[ListNode] = set()

        current_node: Optional[ListNode] = head
        while current_node:
            if current_node in visit_node:
                return True

            visit_node.add(current_node)
            current_node = current_node.next
        return False