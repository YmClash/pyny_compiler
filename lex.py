import sys
import enum


class Lexer:
    def __init__(self, code_source):
        self.code_source = code_source + '\n'
        self.current_character = ''
        self.current_Pos = -1
        self.next_character()


    def next_character(self):
        self.current_Pos += 1
        if self.current_Pos >= len(self.code_source):
            self.current_character = '\0'
        else:
            self.current_character = self.code_source[self.current_Pos]


    def peek(self):
        if self.current_Pos +1 >= len(self.code_source):
            return '\0'
        return self.code_source[self.current_Pos + 1]


    def abort(self, message):
        sys.exit("Lexing error. " + message)
        pass

    def skip_whitespace(self):
        while self.current_character == ' ' or self.current_character == '\t' or self.current_character == '\r':
            self.next_character()


    def skip_comment(self):
        pass

    def get_token(self):
        self.skip_whitespace()
        # check  1st character
        if self.current_character == '+':
            token = Token(self.current_character,TokenType.PLUS)

        elif self.current_character == '-':
            token = Token(self.current_character,TokenType.MINUS)
        elif self.current_character == '*':
            token = Token(self.current_character,TokenType.ASTERISK)
        elif self.current_character == '/':
            token = Token(self.current_character,TokenType.SLASH)
        elif self.current_character == '\n':
            token = Token(self.current_character,TokenType.NEWLINE)
        elif self.current_character == '\0':
            token = Token(self.current_character,TokenType.EOF)
        else:
            self.abort("Unknow token: " + self.current_character)

        self.next_character()
        return token




# token  qui  contient le  type  de  token  et le test original
class Token:
    def __init__(self,tokentext,tokentype):
        self.tokenText = tokentext
        self.tokentype = tokentype


class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDEN = 2
    STRING = 3
    #keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    #operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

