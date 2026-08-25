from typing import Optional
"""
self.next: Optional["Node"]
    "Node": tham chiếu đến class Node chưa được định nghĩa xong.
    Optional["Node"] tương đương Node | None.
"""
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] | None = None

    @staticmethod
    def traverseAndPrint(head: Optional[Node]) -> None:
        currentNode: Optional[Node] = head

        while currentNode is not None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("NULL")
if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    Node.traverseAndPrint(node1)