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

    def insert_at_tail(self, data: int) -> None:
        new_Node: Optional["Node"] = Node(data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            return


        new_Node.prev = self.tail
        self.tail.next = new_Node
        self.tail = new_Node

    def delete_at_head(self) -> None:
        self.head = self.head.next
        self.head.prev = None

    def length(self) -> int:
        count: int = 0
        currentNode: Optional["Node"] = self.head
        while currentNode:
            currentNode = currentNode.next
            count += 1
        return count

    def delete_at_tail(self) -> None:

    # prevNode: Optional["Node"]
    # prevNode = self.tail.prev
    # prevNode.next = None
    # self.tail = prevNode

        if self.tail is None:
            return
        if self.tail == self.head:
            self.tail = self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def delete_at_position(self, position: int) -> None:
        if position < 0:
            return

        if position == 0:
            self.delete_at_head()
            return

        length: int = self.length()
        if position > length:
            return

        if position == length - 1:
            self.delete_at_tail()
            return

        current_node: Optional["Node"] = self.head
        for _ in range(position):
            current_node = current_node.next
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

    def traverse_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("NULL")

if __name__ == "__main__":
    dll: DoublyLinkedList = DoublyLinkedList()

    dll.insert_at_tail(30)
    dll.insert_at_tail(40)
    dll.insert_at_tail(50)
    dll.insert_at_tail(60)
    dll.insert_at_tail(70)
    print("Origin Node:         ", end="")
    dll.traverse_forward()

    dll.delete_at_tail()
    print("Delete Node Tail:    ", end="")
    dll.traverse_forward()

    position: int = 2
    dll.delete_at_position(position)
    print("Delete Node At Position=", position, ":      ", end="")
    dll.traverse_forward()
