'''
create a parser

takes in an array of tokens (that contain input)

returns an array (py list) representation of a binary tree
'''


class Parser:
    """class Parser. base parser"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def __str__(self):
        f"class Parser. base parser"

    # def __repr__(self):
    #     pass

    def move(self):
        """method move: moves the pointer w/i the current string"""
        self.idx += 1
        if self.idx<len(self.tokens):
            self.token = self.tokens[self.idx]

    def factor(self):
        """method factor: defines the `Factor` non-terminal"""
        if self.token.type=="INT" or self.token.type=="FLT":
            return self.token

    def term(self):
        """method term: defines the `term`"""
        left_node = self.factor()
        self.move()
        while self.token.value=="*" or self.token.value=="/":
            op = self.token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, op, right_node]
        return left_node

    def expression(self):
        """ method expression: defines the `expression` """
        left_node = self.term()
        while self.token.value=="+" or self.token.value=="-":
            op = self.token
            self.move()
            right_node = self.term()
            left_node = [left_node, op, right_node]
        return left_node

    def parse(self):
        """method parse: parses the input string"""
        return self.expression()
