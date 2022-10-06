from hon.core import pg

from hon.baseboxs import Attribute, LambdaBox, Comma, MultipleAttribute


@pg.production('comma :')
@pg.production('multiple_attribute_defination : ')
def empty_express(self, expression):
    """allows empty value in the right side of the production."""
    return LambdaBox()


@pg.production('comma : COMMA')
def comma_expression(self, expression):
    """define comma."""
    return Comma()


@pg.production("attribute_defination : ATTRIBUTE ASSIGNMENT_OPERATOR STRING ")
def attribute_defination(state, expression):
    """
    Defination of a single attribute.

    ex: class = "btn btn-success"
    """
    return Attribute(expression[0].getstr(), expression[2].getstr())

@pg.production("multiple_attribute_defination : attribute_defination comma multiple_attribute_defination")
def multiple_attribute_defination(state, expression):
    """
    Defination of multiple attribute assignment.

    ex: class = "mx-0", id="main"
    """
    return MultipleAttribute(
        filter(lambda exp: isinstance(exp, (Attribute, MultipleAttribute)), expression)
    )

parser = pg.build()

