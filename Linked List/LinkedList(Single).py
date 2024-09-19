class Node():

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked():
    def __init__(self):
        self.head = None
        self.n = 0

    def length(self):
        return self.n

    def adds(self,item):
        self.n += 1
        new = Node(item)
        current = self.head
        if current == None:
            self.head = new
        else:
            while current.next != None:
                current = current.next
            current.next = new

    def removes(self, item):
        self.n -= 1
        current = self.head
        if current.data == item:
            self.head = current.next
        else:
            while current.next.data != item:
                current = current.next
            current.next = current.next.next

    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def find(self, position):
        current = self.head
        if position == 0:
            return self.head.data
        else:
            index = 0
            while current != None:
                if index == position:
                    return current.data
                index += 1
                current = current.next
        return None

    def position(self, item):
        index = 0
        current = self.head
        if current.data == item:
            return 0
        while current != None:
            if current.data == item:
                return index
            index += 1
            current = current.next




a = Linked()

a.adds("A1")
a.adds("A2")
a.adds("A3")
a.adds("A4")
a.adds("A5")
a.adds("A6")
a.adds("A7")

a.removes("A7")

a.display()

print('Size:', a.length())

item = 'A4'
print(f"Item {item}: Index", a.position(item))

index = 2
print(f"Index {index}: Item", a.find(index))



