from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class DoubleLinkedList:
    @staticmethod
    def traverse_forward(head: Optional["Node"]):
        currentNode: Optional["Node"] = head
        while currentNode:
            print(currentNode.data, end=" <-> ")
            currentNode = currentNode.next
        print("NULL")

    @staticmethod
    def traverse_backward(tail: Optional["Node"]):
        currentNode: Optional["Node"] = tail

        while currentNode:
            print(currentNode.data, end=" <-> ")
            currentNode = currentNode.prev

        print("NULL")

if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node2.prev = node1
    node3.prev = node2
    node4.prev = node3

    DoubleLinkedList.traverse_forward(node1)
    DoubleLinkedList.traverse_backward(node4)