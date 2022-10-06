import re

from rply.token import BaseBox

from hon.constants import Token


class ValueBox(BaseBox):
    def eval(self):
        return self.value


class LambdaBox(ValueBox):
    def __init__(self):
        self.value = None


class String(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.strip("'\"")


class AttributeName(BaseBox):
    def __init__(self, name):
        self.name = name

    def eval(self):
        return self.name.lower()


class AssignmentOperator(ValueBox):
    def __init__(self):
        self.value = "="

    def eval(self):
        return self.value


class Comma(ValueBox):
    def __init__(self):
        self.value = ","


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


class MultipleAttribute(BaseBox):
    def __init__(self, attributes):
        self.attributes = attributes

    def eval(self):
        return " ".join(attribute.eval() for attribute in self.attributes)


class Bracket(BaseBox):
    def __init__(self, expression):
        self.expression = expression.eval()

    def eval(self):
        pattern = r'([a-zA-Z]+[a-zA-Z\-]*=["|\'][^"\\|\\.]*["|\'])'
        return tuple(re.findall(pattern, self.expression))


class MultipleBracket(BaseBox):
    def __init__(self, brackets):
        self.brackets = brackets

    def eval(self):
        brackets = []
        for bracket in self.brackets:
            if isinstance(bracket, Bracket):
                brackets.append(bracket.eval())
            else:
                brackets.extend(bracket.eval())
        return brackets
