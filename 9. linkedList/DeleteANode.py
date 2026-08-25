from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] | None = None

    def traverseAndPrint(self, head: Optional["Node"]) -> None:
        currentNode: Optional[Node] = head

        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("NULL")

    @staticmethod
    def deleteSpecificNode(head: Optional["Node"], nodeToDelete: Optional["Node"]) -> Optional["Node"]:
        if head is nodeToDelete:
            return head.next

        currentNode: Optional["Node"] = head
        while currentNode.next and currentNode.next != nodeToDelete:
            currentNode = currentNode.next

        if currentNode.next is None:
            return head

        currentNode.next = currentNode.next.next

        return head

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

    print("Before deletion:")
    n.traverseAndPrint(node1)

    node_test: Optional["Node"] = n.deleteSpecificNode(node1, node4)

    print("\nAfter deletion:")
    n.traverseAndPrint(node_test)


