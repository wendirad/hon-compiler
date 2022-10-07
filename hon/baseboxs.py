from rply.token import BaseBox


class ValueBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class LambdaBox(ValueBox):
    def __init__(self, value=None):
        self.value = value = getattr(self, "value", None)  # noqa: F841


class Expression(ValueBox):
    def eval(self):
        return "".join((expression.eval() for expression in self.value))


class LeftBrace(LambdaBox):
    value = "{"


class RightBrace(LambdaBox):
    value = "}"


class LeftBracket(LambdaBox):
    value = "["


class RightBracket(LambdaBox):
    value = "]"


class LeftParentheses(LambdaBox):
    value = "("


class RightParentheses(LambdaBox):
    value = ")"


class Comma(LambdaBox):
    value = ","


class AssignmentOperator(LambdaBox):
    value = "="


class String(ValueBox):
    def eval(self):
        return self.value.strip("'\"")


class VariableName(ValueBox):
    def eval(self):
        return self.value.lstrip("%%").lower()


class VariableAccess(ValueBox):
    def eval(self):
        return self.value.lstrip("%").lower()


class AttributeName(ValueBox):
    def eval(self):
        return self.value.lower()


class Attribute(BaseBox):
    def __init__(self, attr_name, operator, value):
        self.attr_name = attr_name
        self.operator = operator
        self.value = value

    def eval(self):
        return '{}{}"{}"'.format(
            self.attr_name.eval(), self.operator.eval(), self.value.eval()
        )


class MultipleAttribute(ValueBox):
    def eval(self):
        return " ".join((attribute.eval() for attribute in self.value))


class TagName(ValueBox):
    def eval(self):
        return self.value.strip(":"), self.is_self_closing()

    def is_self_closing(self):
        return self.value.endswith(":")


class Bracket(ValueBox):
    def eval(self):
        return " ".join((attribute.eval() for attribute in self.value))


class MultipleBracket(ValueBox):
    def eval(self):
        brackets = []
        for bracket in self.value:
            if isinstance(bracket, Bracket):
                brackets.append(bracket.eval())
            else:
                brackets.extend(bracket.eval())
        return brackets


class EmptyTag(BaseBox):
    def __init__(self, tag_name):
        self.name, self.is_self_closing = tag_name.eval()

    def eval(self):
        tag = "<{0} />" if self.is_self_closing else "<{0}></{0}>"
        return tag.format(self.name)


class Tag(BaseBox):
    def __init__(self, tag_name, attribute):
        self.name, self.is_self_closing = tag_name.eval()
        self.attribute = attribute

    def eval(self):
        tag = "<{0} {1} />" if self.is_self_closing else "<{0} {1}></{0}>"
        return tag.format(self.name, self.attribute.eval())


class ParenthesesTag(BaseBox):
    def __init__(self, tag_name, attributes):
        self.tag_name = tag_name
        self.attributes = attributes

    def eval(self):
        value = ""
        for attribute in self.attributes:
            if isinstance(attribute, Bracket):
                value += Tag(self.tag_name, attribute).eval()
            else:
                for attr in attribute.eval():
                    value += Tag(self.tag_name, ValueBox(attr)).eval()
        return value


class Content(BaseBox):
    def __init__(self, tag, expression):
        self.tag = tag
        self.expression = expression

    def eval(self):
        return self.tag.eval().replace(
            "></", ">{}</".format(self.expression.eval())
        )
