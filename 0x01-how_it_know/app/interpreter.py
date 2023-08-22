'''
create an interpreter

takes in an array (the tree) that contains input

traverses the "tree" post-order

returns an array (py list) representation of a binary tree
'''

from tokens import Integer, Float, Keyword


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

        #evaluate conditionals
        if isinstance(tree, list):
            if isinstance(tree[0], Keyword):
                if tree[0].value=="if":
                    for idx, condition in enumerate(tree[1][0]):
                        evaluation = self.interpret(condition)
                        print(evaluation)
                        if evaluation.value==1:
                            return self.interpret(tree[1][1][idx])
                    if len(tree[1])==3:
                        return self.interpret(tree[1][2])
                    else:
                        return
        #evaluate unary ops
        if isinstance(tree, list) and len(tree)==2:
            expression = tree[1]
            if isinstance(expression, list):
                expression = self.interpret(expression)
            return self.compute_unary(tree[0], expression)
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
        elif op.value==">":
            output = 1 if left > right else 0
        elif op.value==">=":
            output = 1 if left >= right else 0
        elif op.value=="<":
            output = 1 if left < right else 0
        elif op.value=="<=":
            output = 1 if left <= right else 0
        elif op.value=="?=":
            output = 1 if left == right else 0
        elif op.value=="and":
            output = 1 if left and right else 0
        elif op.value=="or":
            output = 1 if left or right else 0

        return Integer(output) if (left_type=="INT" and right_type=="int") else Float(output)

    def compute_unary(self, operator, operand):
        """method compute_unary: computes unary ops"""
        operand_type = "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value) 

        if operator.value=="+":
            output = +operand
        elif operator.value=="-":
            output = -operand
        elif operator.value=="not":
            output = 1 if not operand else 0

        return Integer(output) if (operand_type=="INT") else Float(output)   