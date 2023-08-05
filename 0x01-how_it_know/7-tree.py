'''
implement a binary tree in py

binary tree: a collection of nodes and edges; each node
has, at most, two edges

node: a data point in the tree

edge: a link from a parent to child node and vv
'''

class Node:
    """class Node: node w/i a binary tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    """class Tree: binary tree"""
    def __init__(self, root):
        self.root = Node(root)

    def pre_order(self, start, records: list):
        """ pre-order traversal """
        # root -> left -> right
        if start is not None:
            records.append(start.val)
            records = self.pre_order(start.left, records)
            records = self.pre_order(start.right, records)
        return records

    def post_order(self, start, records: list):
        """"post-order traversal"""
        #left -> right -> root
        if start is not None:
            records = self.post_order(start.left, records)
            records = self.post_order(start.right, records)
            records.append(start.val)
        return records
    
tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(1)
tree.root.right.left = Node('text')
tree.root.right.right = Node(True)

#      5
#   /      \
#  3        4
# / \     /   \
#2   1 'text' True

#preorder -> [5, 3, 2, 1, 4, 'text', True]
print(tree.pre_order(tree.root, []))

#postorder -> [2, 1, 3, 'text', True, 4, 5]
print(tree.post_order(tree.root, []))
