class Token:
    """class Token: base token"""
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return str(self.value)


class Integer(Token):
    """"class Integer: token of type int"""
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    """"class Float: token of type float"""
    def __init__(self, value):
        super().__init__("FLT", value)


class String(Token):
    """"class String: token of type str"""
    def __init__(self, value):
        super().__init__("STR", value)


class Operator(Token):
    """"class Operator: token of type op"""
    def __init__(self, value):
        super().__init__("OP", value)


class Reserved(Token):
    """"class Reserved: token of type str, reserved words"""
    def __init__(self, value):
        super().__init__("RSVD", value)

class Variable(Token):
    """"class Variable: token of type str, variables"""
    def __init__(self, value):
        super().__init__("VAR(?)", value)