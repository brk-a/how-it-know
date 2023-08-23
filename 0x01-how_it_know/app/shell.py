from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("FrankenScript: ~/$:  ")
    tokeniser = Lexer(text)
    tokens = tokeniser.tokenise()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
        print(result)