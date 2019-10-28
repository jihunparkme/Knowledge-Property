# Node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly linked list
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    # Add new node at the end of the linked list
    def enqueue(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return -1

        v = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        return v

    # print
    def print(self):
        obj = self.head
        string = ""
        while obj:
            string += str(obj.data)
            if obj.next:
                string += " -> "
            obj = obj.next
        print(string)


if __name__ == "__main__":
    list = LinkedList()
    # Add object
    list.enqueue(Node(1))
    list.enqueue(Node(2))
    list.enqueue(Node(3))
    list.enqueue(Node(4))
    list.print()  # 1->2->3->4
    # Delete object
    print(list.dequeue())
    print(list.dequeue())
    list.print()  # 3->4