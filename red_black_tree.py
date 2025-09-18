from binary_search_tree import BinarySearchTree, Node

BLACK = 0
RED = 1

class RedBlackNode(Node):
    def __init__(self, data= None ,color= RED):
        super().__init__(data)
        self.color = color


class RBTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        
        self.nil = RedBlackNode(color=BLACK)
        
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil

        self.root = self.nil

    
    def left_rotation(self, node):
        y = node.right
        ...

    
