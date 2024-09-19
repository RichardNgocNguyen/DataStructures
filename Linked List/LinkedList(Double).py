class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def adds(self, item):
        self.n += 1
        new = Node(item)
        current = self.head
        if self.head is None:
            self.head = new
        else:
            while current.next != None:
                current = current.next
            current.next = new
            current.next.prev = current
            self.tail = new

    def remove(self, item):
        self.n -= 1
        if self.head.data == item:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            while current.next.data != item:
                current = current.next
            current.next = current.next.next
            current.next.prev = current

    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def reverse_display(self):
        current = self.tail
        while current != None:
            print(current.data)
            current = current.prev


a = DoubleLinked()

a.adds("A1")
a.adds("A2")
a.adds("A3")
a.adds("A4")
a.adds("A5")
a.adds("A6")
a.adds("A7")
a.remove("A1")
a.remove("A4")
a.remove("A7")

a.display()

print()

a.reverse_display()
