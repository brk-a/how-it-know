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
        elif self.token=="(":
            self.move()
            expression = self.boolean_expression()
            return expression
        elif self.token.value=='not':
            operator = self.token
            self.move()
            return [operator, self.boolean_expression()]
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value=="+" or self.token.value=="-":
            operator = self.token
            self.move()
            operand = self.boolean_expression()
            return [operator, operand]

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
    
    def boolean_expression(self):
        """method boolean_expression: defines the `Boolean` expression"""
        left_node = self.comparison_expression()
        while self.token.type=="BOOL":
            op = self.token
            self.move()
            right_node = self.comparison_expression()
            left_node = [left_node, op, right_node]
        return left_node

    def comparison_expression(self):
        """method comparison_expression: defines the `Comparison` expression"""
        left_node = self.expression()
        while self.token.type=="COMP":
            op = self.token
            self.move()
            right_node = self.expression()
            left_node = [left_node, op, right_node]
        return left_node

    def statement(self):
        """method statement: handles declarations and assignments"""
        if self.token.type=="RSVD":
            self.move()
            left_node = self.variable()
            self.move()
            if self.token.value=="=":
                op = self.token
                self.move()
                right_node = self.boolean_expression()
                return [left_node, op, right_node]
        elif self.token.type=="INT" or self.token.type=="FLT" or self.token.type=="OP" or self.token.value=="not":
            return self.boolean_expression()
        elif self.token.value=="if":
            return [self.token, self.if_statements()]

    # def if_statement(self):
    #     """method if_statement: handles the `do` conditional"""
    #     self.move()
    #     condition = self.boolean_expression()

    #     if self.token.value=="do":
    #         self.move()
    #         action = self.statement()
    #         return condition, action
    #     elif self.tokens[self.idx-1].value=="do":
    #         action = self.statement()
    #         return condition, action
    
    def if_statements(self):
        """method if_statements: handles the `if-elif-else` conditionals"""
        conditions = []
        actions = []
        if_statement = self.if_statement()

        conditions.append(if_statement[0])
        actions.append(if_statement[1])

        while self.token.value=="elif":
            if_statement = self.if_statement()
            conditions.append(if_statement[0])
            actions.append(if_statement[1])
        
        if self.token.value=="else":
            self.move()
            self.move()
            else_action = self.statement()
            return [conditions, actions, else_action]

        return [conditions, actions]

    def if_statement(self):
        """method if_statement: handles the `do` conditional"""
        self.move()
        condition = self.boolean_expression()

        if self.token.value=="do":
            self.move()
            action = self.statement()
            return condition, action
        elif self.tokens[self.idx-1].value=="do":
            action = self.statement()
            return condition, action

    def variable(self):
        """method variable: creates a variable"""
        if self.token.type.startswith("VAR"):
            return self.token
        

    def parse(self):
        """method parse: parses the input string"""
        return self.statement()
