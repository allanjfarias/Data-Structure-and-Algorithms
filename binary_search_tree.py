

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def is_left(self):
        q = self.parent
        if q == None:
            return False

        if q.left == self:
            return True

        return False

    def is_right(self):
        q = self.parent
        if q == None:
            return False

        if q.right == self:
            return True

        return False

    def brother(self):
        if self.parent == None:
            return False

        if self.is_left():
            return self.parent.right

        return self.parent.left

    def __repr__(self):
        return f'{self.data}'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        x = self.root
        y = None

        while x != None:
            y = x

            if x.data > new_node.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y == None:
            self.root = new_node

        elif y.data > new_node.data:
            y.left = new_node

        else:
            y.right = new_node

    def search(self, key):
        x = self.root

        while x != None and key != x.data:
            if key < x.data:
                x = x.left
            else:
                x = x.right

        return x

    def min(self, x=None):
        current = self.root if x is None else x

        if current is None:
            return

        while current.left != None:
            current = current.left

        return current

    def max(self, x=None):
        current = self.root if x is None else x

        if current is None:
            return

        while current.right != None:
            current = current.right

        return current

    def successor(self, data):
        x = self.search(data)

        if x is None:
            return

        if x.right != None:
            return self.min(x.right)

        y = x.parent

        while y != None and x.is_right():
            x = y
            y = y.father

        return y

    def predecessor(self, data):
        x = self.search(data)

        if x is None:
            return

        if x.left != None:
            return self.max(x.left)

        y = x.parent

        while y != None and x.is_left():
            x = y
            y = y.father

        return y

    def transplant(self, u, v):

        if u.father == None:
            self.root = v

        elif u.is_left():
            u.father.left = v
        else:
            u.father.right = v

        if v != None:
            v.father = u.father

    def delete(self, data):
        z = self.search(data)

        if z == None:
            return

        if z.left == None:
            self.transplant(z, z.right)

        elif z.right == None:
            self.transplant(z, z.left)

        else:
            y = self.min(z.right)
            if y != z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.father = y

            self.transplant(z, y)
            y.left = z.left
            y.left.father = y

    def in_order(self, root, array=[]):

        if root != None:
            self.in_order(root.left)
            array.append(root.data)
            self.in_order(root.right)

        return array

    def pre_order(self, node, array=[]):

        if node != None:
            array.append(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

        return array

    def pos_order(self, node, array=[]):

        if node != None:
            self.pos_order(node.left)
            self.pos_order(node.right)
            array.append(node.data)
        return array


if __name__ == '__main__':
    tree = BinarySearchTree()
    data_to_insert = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    for x in data_to_insert:
        tree.insert(x)

    tree.delete(20)
    tree.delete(9)
    tree.delete(18)
    tree.delete(6)
    tree.delete(15)

    in_order = tree.in_order(tree.root)
    pre_order = tree.pre_order(tree.root)
    pos_order = tree.pos_order(tree.root)

    print(f'In-Order: {in_order}', end='\n')
    print(f'Pre-Order: {pre_order}', end='\n')
    print(f'Pos-Order: {pos_order}', end='\n')
