class Node:
    def __init__(self, data):
        self.p = None
        self.left = None
        self.right = None
        self.data = data

    def is_right(self):
        q = self.p
        return q is not None and q.right == self

    def is_left(self):
        q = self.p
        return q is not None and q.left == self

    def brother(self):
        q = self.p

        if q is None:
            return

        elif self.is_right():
            return q.left

        return q.right

    def __repr__(self):
        return f"Node: {self.data}"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self, start_node):
        x = self.root if start_node is None else start_node

        while x.left is not None:
            x = x.left

        return x

    def max(self, start_node):
        x = self.root if start_node is None else start_node

        while x.right is not None:
            x = x.right

        return x

    def in_order_walk(self,
                      node,
                      visit=lambda x: print(x.data)
                      ):

        if node is not None:
            self.in_order_walk(node.left, visit)
            visit(node)
            self.in_order_walk(node.right, visit)

    
    def pre_order_walk(self,
                       node,
                       visit=lambda x: print(x.data)
                       ):
        
        if node is not None:
            visit(node)
            self.pre_order_walk(node.left, visit)
            self.pre_order_walk(node.right, visit)

    
    def pos_order_walk(self,
                       node,
                       visit=lambda x: print(x.data)
                       ):
        
        if node is not None:
            self.pos_order_walk(node.left, visit)
            self.pos_order_walk(node.right, visit)
            visit(node)

    
    def successor(self, node):
        x = self.search(node)

        if x is None:
            return

        elif x.right is not None:
            return self.min(x.right)

        y = x.p

        while y is not None and x.is_right():
            x = y
            y = y.p

        return y

    def predecessor(self, node):
        x = self.search(node)

        if x is None:
            return

        elif x.left is not None:
            return self.max(x.left)

        y = x.p

        while y is not None and x.is_left():
            x = y
            y = y.p

        return y

    def search(self, key):
        x = self.root

        while x is not None and x.data != key:
            if key > x.data:
                x = x.right

            else:
                x = x.left

        return x

    def insert(self, data):
        z = Node(data)
        x = self.root
        y = None

        while x is not None:
            y = x

            if data > x.data:
                x = x.right

            else:
                x = x.left

        z.p = y

        if y is None:
            self.root = z

        elif data > y.data:
            y.right = z

        else:
            y.left = z

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        
        elif u.is_right():
            u.p.right = v
        
        else:
            u.p.left = v

        if v is not None:
            v.p = u.p

    def delete(self, data):
        z = self.search(data)

        if z is None:
            return

        if z.left is None:
            self.transplant(z, z.right)

        elif z.right is None:
            self.transplant(z, z.left)

        else:
            y = self.min(z.right)

            if y != z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.transplant(z, y)
            z.left.p = y
            y.left = z.left


if __name__ == '__main__':
    tree = BinarySearchTree()
    data_to_insert = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

    for x in data_to_insert:
        tree.insert(x)

    tree.in_order_walk(tree.root)
    tree.pre_order_walk(tree.root)
    tree.pos_order_walk(tree.root)
