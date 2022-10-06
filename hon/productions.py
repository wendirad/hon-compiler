from hon.baseboxs import (
    Attribute,
    Bracket,
    Comma,
    LambdaBox,
    MultipleAttribute,
    MultipleBracket,
)
from hon.core import pg


@pg.production("expression : parentheses_defination")
def expression(state, expression):
    return expression[0]


@pg.production("comma :")
@pg.production("multiple_attribute_defination :")
@pg.production("mulitple_bracket_defination :")
def empty_expression(self, expression):
    """allows empty value in the right side of the production."""
    return LambdaBox()


@pg.production("comma : COMMA")
def comma_expression(self, expression):
    """define comma."""
    return Comma()


@pg.production("attribute_defination : ATTRIBUTE ASSIGNMENT_OPERATOR STRING")
def attribute_defination(state, expression):
    """
    Defination of a single attribute.

    ex: class = "btn btn-success"
    """
    return Attribute(expression[0].getstr(), expression[2].getstr())


@pg.production(
    "multiple_attribute_defination : attribute_defination comma multiple_attribute_defination"
)
def multiple_attribute_defination(state, expression):
    """
    Defination of multiple attribute assignment.

    ex: class = "mx-0", id="main"
    """
    return MultipleAttribute(
        filter(
            lambda exp: isinstance(exp, (Attribute, MultipleAttribute)),
            expression,
        )
    )


@pg.production(
    "bracket_defination : LEFT_BRACKET multiple_attribute_defination RIGHT_BRACKET"
)
def bracket_defination(state, expression):
    """
    Defination of attribues inside bracket

    ex: [class = "mx-0", id="main"]
    """
    return Bracket(expression[1])


@pg.production(
    "mulitple_bracket_defination : bracket_defination comma mulitple_bracket_defination"
)
def multiple_bracket_defination(state, expression):
    """
    Defination of multiple bracket attributes

    ex: [x="1"],[y="3"]
    """
    return MultipleBracket(
        filter(
            lambda exp: isinstance(exp, (Bracket, MultipleBracket)),
            expression,
        )
    )

@pg.production('parentheses_defination : LEFT_PARA mulitple_bracket_defination RIGHT_PARA')
def parentheses_defination(state, expression):
    """
    Defination of mutiple bracket inside parantheses
    """
    return expression[1]

parser = pg.build()
