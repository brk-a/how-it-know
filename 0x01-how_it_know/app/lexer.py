'''
create a lexer (lexical analyser)

takes in a string that contains input

returns an array (py list) of tokens
'''

from tokens import Integer, Operator, Float, Reserved, Variable, Boolean, Comparison


class Lexer:
    """class Lexer: analyser"""
    DIGITS = "0123456789"
    LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OPS = "+-*/%()="
    STOPWORDS = [" ",]
    RESERVEDWORDS =  ['make', ]
    BOOLS = ['and', 'or', 'not']
    COMAPRISONS = ['>', '<', '>=', '<=', '?=']
    SPECIALCHARS = "><=?"

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
            elif self.char in Lexer.LETTERS:
                word = self.extract_word()

                if word in Lexer.RESERVEDWORDS:
                    self.token = Reserved(word)
                elif word in Lexer.BOOLS:
                    self.token = Boolean(word)
                else:
                    self.token = Variable(word)
            elif self.char in Lexer.SPECIALCHARS:
                comparator = ""
                while self.char in Lexer.SPECIALCHARS and self.idx<len(self.text):
                    comparator += self.char
                    self.move()
                self.token = Comparison(comparator)

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
    
    def extract_word(self):
        """method extract_word: extracts chars required to create a token"""
        word = ""
        while self.char in Lexer.LETTERS and self.idx<len(self.text):
            word += self.char
            self.move()

        return word

    def move(self):
        """method move: moves the pointer w/i the current string"""
        self.idx += 1
        if self.idx<len(self.text):
            self.char = self.text[self.idx]
