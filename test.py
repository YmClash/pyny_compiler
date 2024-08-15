import re

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return ('INTEGER', self.integer())

            if self.current_char == '+':
                self.advance()
                return ('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return ('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return ('MUL', '*')

            if self.current_char == '/':
                self.advance()
                return ('DIV', '/')

            if self.current_char == '(':
                self.advance()
                return ('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return ('RPAREN', ')')

            self.error()

        return ('EOF', None)

# Exemple d'utilisation
text = "3 +  * ( 10 - 20 )"
lexer = Lexer(text)

for token in iter(lexer.get_next_token, ('EOF', None)):
    print(token)
