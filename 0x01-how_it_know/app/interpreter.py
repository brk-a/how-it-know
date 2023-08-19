'''
create an interpreter

takes in an array (the tree) that contains input

traverses the "tree" post-order

returns an array (py list) representation of a binary tree
'''

from tokens import Integer, Float


class Interpreter:
    """class Interpreter: base interpreter"""
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    def interpret(self, tree=None):
        """method interprete. creates nodes for compute_bin"""
        if tree is None:
            tree = self.tree

        #evaluate unary ops
        if isinstance(tree, list) and len(tree)==2:
            return self.compute_unary(tree[0], tree[1])
        #evaluate no op
        elif not isinstance(tree, list):
            return tree
        else:
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

    def read_VAR(self, id):
        """method read_VAR. getter fn to read variables"""
        variable = self.data.read(id)
        variable_type = variable.type

        return  getattr(self, f"read_{variable_type}")(variable.value)
        
    def compute_bin(self, left, op, right):
        """method compute_bin: computes arithmetic expressions"""
        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)

        if op.value=="=":
            left.type = f"VAR({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

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
        elif op.value=="%":
            output = left % right

        return Integer(output) if (left_type=="INT" and right_type=="int") else Float(output)

    def compute_unary(self, operator, operand):
        """method compute_unary: computes unary ops"""
        operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value) 

        if operator.value=="+":
            return +operand
        if operator.value=="-":
            return -operand      