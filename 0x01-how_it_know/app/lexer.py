'''
create a lexer (lexical analyser)

takes in a string that contains input

returns an array (py list) of tokens
'''

class Lexer:
    """class Lexer: analyser"""
    DIGITS = "0123456789"
    OPS = "+-*/%"
    STOPWORDS = [" ",]

    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = [] #array of tokens is `[]` by default
        self.token = None #current token is `None` by default
        self.char = self.text[self.idx]

    def __str__(self):
        return f"class Lexer. Base analyser"

    def tokenise(self):
        """ method tokenise: creates tokens from input `text` """
        while self.idx<len(self.text):
            if self.char in Lexer.DIGITS:
                self.token = self.extract_number()
            elif self.char in Lexer.OPS:
                self.token = Operator(self.char)
                self.move()
            elif self.char in Lexer.STOPWORDS:
                self.move()
                continue

            self.tokens.append(self.token)
            
        return self.tokens
    
    def extract_number(self):
        """method extract_number: extracts chars required to create a token"""
        number = ""
        isFloat = False
        while (self.char in Lexer.DIGITS or self.char==".") and (self.idx<len(self.text)):
            if self.char==".":
                isFloat = True
            number += self.char
            self.move()

        return Integer(number) if not isFloat else Float(number)

    def move(self):
        """method move: moves the pointer w/i the current string"""
        self.idx += 1
        if self.idx<len(self.text):
            self.char = self.text[self.idx]


class Token:
    """class Token: base token"""
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return self.value


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


# class Integer(Token):
#     """"class Integer: token of type int"""
#     def __init__(self, value):
#         super().__init__("INT", value)