from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None

    def insert_at_head(self, data: int) -> None:
        new_Node: Optional["Node"] = Node(data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            return

        new_Node.next = self.head
        self.head.prev = new_Node
        self.head = new_Node

    def insert_at_tail(self, data: int) -> None:
        new_Node: Optional["Node"] = Node(data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            return

        new_Node.prev = self.tail
        self.tail.next = new_Node
        self.tail = new_Node

    def length(self) -> int:
        count: int = 0
        current: Optional["Node"] = self.head
        while current is not None:
            current = current.next
            count += 1
        return count


    def insert_at_position(self, data: int, position: int) -> None:
        if position < 0: return

        if position == 0:
            self.insert_at_head(data)
            return

        length: int = self.length()

        if position > length:
            return

        if position == length:
            self.insert_at_tail(data)
            return

        currentNode: Optional["Node"] = self.head
        for _ in range(position - 1):
            currentNode = currentNode.next

        new_node: Optional["Node"] = Node(data)

        new_node.next = currentNode.next
        new_node.prev = currentNode

        currentNode.next.prev = new_node
        currentNode.next = new_node


    def traverse_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("NULL")

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_head(30)
    dll.insert_at_head(20)
    dll.insert_at_head(10)
    dll.insert_at_head(5)

    dll.insert_at_tail(40)
    dll.insert_at_tail(50)

    print("Traverse Forward:        ", end="")
    dll.traverse_forward()

    position: int = 6
    print("Insert at position=", position, ":   ", end="")
    dll.insert_at_position(40, position)
    dll.traverse_forward()