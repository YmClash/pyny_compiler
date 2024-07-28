import re


class Token:
    END_OF_FILE = 'EOF'
    DEF = 'DEF'
    EXTERN = 'EXTERN'
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'


class Lexxer:
    def __init__(self, code_source):
        self.code_source = code_source + '\n'
        self.current_Pos = -1
        self.current_character = self.code_source[self.current_Pos] if self.current_Pos < len(self.code_source) else '\0'

    def advance(self):
        self.current_Pos += 1
        self.current_character = self.code_source[self.current_Pos] if self.current_Pos < len(self.code_source) else '\0'
        pass

    def skip_whitespace(self):
        while self.current_character is not None and self.current_character.isspace():
            self.advance()


    def get_next_token(self):
        pass


