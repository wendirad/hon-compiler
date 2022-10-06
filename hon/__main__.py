import argparse

from hon.core import lexer
from hon.productions import parser

class ParserState(object):
    def __init__(self, variables):
        self.variables = variables

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("infile", type=argparse.FileType("r"))
input_code = arg_parser.parse_args(["-"]).infile.read()

data = {}
tokens = lexer.lex(input_code)
ast = parser.parse(tokens, state=ParserState(data))
