class Node:
    def __init__(self, item=None):
        self.data = item
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree_Linked:
    def __init__(self):
        self.root = None
        self.n = 0

    def build_bst(self, array):
        # Creates the binary tree with first element as root
        for i in range(len(array)):
            self.insert(array[i])

    def insert(self, item):
        self.n += 1
        # Creates node objects
        node = Node(item)
        current = self.root
        # If root is not established, set it to node object
        if self.root is None:
            self.root = node
        # Otherwise travel down the bst until the variable current is in the correct spot
        else:
            # As long as there is a left or right node to travel down to
            while current.left != None or current.right != None:
                # If new node value is <= current node value and there is a left node to travel to
                if node.data <= current.data and current.left != None:
                    current = current.left
                # If new node value is > current node value and there is a right node to travel to
                elif node.data > current.data and current.right != None:
                    current = current.right
                # Otherwise end loop
                else:
                    break

            # If new node value <= than current node value, set it to left of that node and set its parent
            if node.data <= current.data:
                current.left = node
                current.left.parent = current
            # If new node value > than current node value, set it to right of that node and set its parent
            elif node.data > current.data:
                current.right = node
                current.right.parent = current

    def remove(self, item):
        def case_1(node):
            parent = node.parent
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
            del node

        def case_2(node):
            parent = node.parent
            if node == parent.left:
                if node.left != None:
                    parent.left = node.left
                elif node.right != None:
                    parent.left = node.right
            elif node == parent.right:
                if node.left != None:
                    parent.right = node.left
                elif node.right != None:
                    parent.right = node.right
            del node

        def case_3(node):
            successor = self.tree_successor(node)
            # Node becomes the successor, and successor becomes the node that we want to delete
            node.data, successor.data = successor.data, node.data
            # Delete the successor that became the node we want to delete
            if successor.left == None and successor.right == None:
                case_1(successor)
            elif successor.left != None or successor.right != None:
                case_2(successor)

        node = self.tree_search(item)
        if node == "Not Exist":
            return

        # Case 1: Has no children, remove node
        if node.left == None and node.right == None:
            case_1(node)
        # Case 2: Has one child, Connect parent to the one child of node
        if node.left == None or node.right == None:
            case_2(node)
        # Case 3: Has two children. Swap x with successor Perform case 1 or 2 to delete x
        if node.left != None and node.right != None:
            case_3(node)

    def tree_search(self, item):
        path = []
        current = self.root
        # Return root if data we want is in root
        if item == current.data:
            return current
        # Move left if data we want is <= current data, Move right if data we want is > current data
        while current.left != None or current.right != None:
            if item < current.data:
                current = current.left
                path.append(0)
            elif item > current.data:
                current = current.right
                path.append(1)
            if item == current.data:
                return current
        return "Not Exist"

    def tree_successor(self, node: Node):
        # Travels to the right of the parameter node, and take the leftmost node of that
        if node.right != None:
            return self.tree_minimum(node.right)

        successor = node.parent
        # Will travel as long as it can travel up and successor is right side of node
        while successor != None and node == successor.right:
            successor = successor.parent
        return successor

    # Travels to the rightmost node in the tree
    def tree_maximum(self, node: Node):
        while node.right != None:
            node = node.right
        return node

    # Travels to the leftmost node in the tree
    def tree_minimum(self, node: Node):
        while node.left != None:
            node = node.left
        return node

    # Parent, Left, Right
    def pre_order(self, parent: Node):
        if parent is None:
            return
        print(parent.data, end=", ")
        self.pre_order(parent.left)
        self.pre_order(parent.right)

    # Left, Parent, Right
    def in_order(self, parent: Node):
        if parent is None:
            return
        self.in_order(parent.left)
        print(parent.data, end=", ")
        self.in_order(parent.right)

    # Left, Right, Parent
    def post_order(self, parent: Node):
        if parent is None:
            return
        self.post_order(parent.left)
        self.post_order(parent.right)
        print(parent.data, end=", ")


a = BinaryTree_Linked()
b = [40, 30, 50, 25, 35, 45, 60, 15, 28, 55, 70]
a.build_bst(b)
c = a.root

print("In Order")
a.in_order(c)

print("\nPre Order")
a.pre_order(c)

print("\nPost Order")
a.post_order(c)

print("\n\nInserting Node")
item = 75
a.insert(item)
print(f"Created Node Object with item:{item}")

print("\nCheck for Working Insert")
a.in_order(c)

print("\n\nRemoving Node")
item = 45
a.remove(item)
print(f"Removed Node Object with item:{item}")

print(f"\nCheck for Working Remove of {item}(Case 1)")
a.in_order(c)

print("\n\nRemoving Node")
item = 50
a.remove(item)
print(f"Removed Node Object with item:{item}")

print(f"\nCheck for Working Remove of {item}(Case 2)")
a.in_order(c)

print("\n\nRemoving Node")
item = 30
a.remove(item)
print(f"Removed Node Object with item:{item}")

print(f"\nCheck for Working Remove of {item}(Case 3)")
a.in_order(c)

print("\n\nSearching Element")
d = a.tree_search(40)
print(f"Node pointing to {d.data} is {d}.")

print("\nSuccessor to Chosen Node")
e = a.tree_successor(d)
print(f"Node {d} -> {d.data} \nSuccessor is \nNode {e} -> {e.data}")
