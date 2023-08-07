'''
create an interpreter

takes in an array (the tree) that contains input

traverses the "tree" post-order

returns an array (py list) representation of a binary tree
'''

from tokens import Integer, Float


class Interpreter:
    """class Interpreter: base interpreter"""
    def __init__(self, tree):
        self.tree = tree

    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    def interpret(self, tree=None):
        """method interprete. creates nodes for compute_bin"""
        if tree is None:
            tree = self.tree

        #evaluate left sub-tree
        left_node = tree[0]
        left_node = self.interpret(left_node) if isinstance(left_node, list) else left_node

        #evaluate right sub-tree
        right_node = tree[-1]
        right_node = self.interpret(right_node) if isinstance(right_node, list) else right_node

        #evaluate root node
        op = tree[1]
        
        
        return self.compute_bin(left_node, op, right_node)

    def read_INT(self, value):
        """method read_INT. getter fn to read ints"""
        return int(value)

    def read_FLT(self, value):
        """method read_FLT. getter fn to read floats"""
        return float(value)

    def compute_bin(self, left, op, right):
        """method compute_bin: computes arithmetic expressions"""
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if op.value=="+":
            output = left + right
        elif op.value=="-":
            output = left - right
        elif op.value=="*":
            output = left * right
        elif op.value=="/":
            output = left / right

        return Integer(output) if (left_type=="INT" and right_type=="int") else Float(output)