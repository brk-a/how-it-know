from lexer import Lexer

while True:
    text = input("FrankenScript: ~/$:  ")
    tokeniser = Lexer(text)
    tokens = tokeniser.tokenise()
    print(tokens)