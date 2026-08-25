# Find The Lowest Value in a Linked List
from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] | None = None

    def findLowestValue(self, head: Optional[Node]) -> int:
        minValue: int = head.data
        currentNode: Optional[Node] = head.next

        while currentNode:
            if currentNode.data < minValue:
                minValue = currentNode.data
            currentNode = currentNode.next

        return minValue

if __name__ == "__main__":
    n: Node = Node(7)
    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("The lowest value in the linked list is:", n.findLowestValue(node1))