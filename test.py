from lex import *




source_code = "+- */"

lexer = Lexer(source_code)

token = lexer.get_token()
while token.tokentype != TokenType.EOF:
    print(token.tokentype)
    token = lexer.get_token()


# while lexer.peek() != '\0':
#     print(lexer.current_character)
#     lexer.next_character()



