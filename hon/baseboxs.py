from rply.token import BaseBox

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
            String(self.value).eval()
        )

class MultipleAttribute(BaseBox):
    def __init__(self, attributes):
        self.attributes = attributes

    def eval(self):
        return ' '.join((attribute.eval() for attribute in self.attributes))
