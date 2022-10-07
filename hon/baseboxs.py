import re

from rply.token import BaseBox

from hon.constants import Token

class ValueBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class LambdaBox(ValueBox):
    def __init__(self):
        self.value = getattr(self, 'value', None)

class LeftBrace(LambdaBox):
    value = '{'

class RightBrace(LambdaBox):
    value = '}'

class LeftBracket(LambdaBox):
    value = '['

class RightBracket(LambdaBox):
    value = ']'

class LeftParentheses(LambdaBox):
    value = '('

class RegihtParentheses(LambdaBox):
    value = ')'

class Comma(LambdaBox):
    value = ','

class AssignmentOperator(LambdaBox):
    value = '='

class String(ValueBox):
    def eval(self):
        return self.value.strip("'\"")

class Variable(ValueBox):
    def eval(self):
        return self.value.lstrip("%%")


class Attribute(BaseBox):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        return '{}{}"{}"'.format(
            AttributeName(self.name).eval(),
            AssignmentOperator().eval(),
            String(self.value).eval(),
        )
