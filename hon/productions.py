# :noqa F405

from hon.baseboxs import *
from hon.core import pg


@pg.production("expression : multiple_tag")
# @pg.production("expression : parentheses_tag")
def expression(state, exp):
    return exp[0]


@pg.production("comma : ")
@pg.production("multiple_variable_access : ")
@pg.production("multiple_attribute_definition : ")
@pg.production("multiple_bracket_definition : ")
@pg.production("multiple_tag : ")
def empty_expression(state, exp):
    return LambdaBox()


@pg.production("left_brace : LEFT_BRACE")
def left_brace(state, exp):
    return LeftBrace(exp[0].getstr())


@pg.production("right_brace : RIGHT_BRACE")
def right_brace(state, exp):
    return RightBrace(exp[0].getstr())


@pg.production("left_bracket : LEFT_BRACKET")
def left_bracket(state, exp):
    return LeftBracket(exp[0].getstr())


@pg.production("right_bracket : RIGHT_BRACKET")
def right_bracket(state, exp):
    return RightBracket(exp[0].getstr())


@pg.production("left_parentheses : LEFT_PARA")
def left_parentheses(state, exp):
    return LeftParentheses(exp[0].getstr())


@pg.production("right_parentheses : RIGHT_PARA")
def right_parentheses(state, exp):
    return RightParentheses(exp[0].getstr())


@pg.production("comma : COMMA")
def comma(state, exp):
    return Comma(exp[0].getstr())


@pg.production("assignment_operator : ASSIGNMENT_OPERATOR")
def assignment_operator(state, exp):
    return AssignmentOperator(exp[0].getstr())


@pg.production("string : STRING")
def string(state, exp):
    return String(exp[0].getstr())


@pg.production("variable : VARIABLE")
def variable(state, exp):
    return VariableName(exp[0].getstr())


@pg.production("variable_definition : variable assignment_operator string")
def variable_definition(state, exp):
    variable, _, value = exp
    state.variables[variable.eval()] = value.eval()
    return value


@pg.production("variable_access : VAR_ACCESS")
def variable_access(state, exp):
    variable = VariableAccess(exp[0].getstr()).eval()
    return String(state.variables.get(variable, ""))


@pg.production(
    "multiple_variable_access : variable_access multiple_variable_access"
)
def multiple_variable_access(state, exp):
    return MultipleVariableAccess(
        filter(lambda ep: not isinstance(ep, LambdaBox), exp)
    )


@pg.production("attribute_name : ATTRIBUTE")
def attribute_name(state, exp):
    return AttributeName(exp[0].getstr())


@pg.production(
    "attribute_definition : attribute_name assignment_operator string"
)
@pg.production(
    "attribute_definition : attribute_name assignment_operator variable_definition"
)
@pg.production(
    "attribute_definition : attribute_name assignment_operator multiple_variable_access"
)
def attribute_definition(state, exp):
    return Attribute(*exp)


@pg.production(
    "multiple_attribute_definition : attribute_definition comma multiple_attribute_definition"
)
def multiple_attribute_definition(state, exp):
    return MultipleAttribute(
        filter(lambda ep: not isinstance(ep, LambdaBox), exp)
    )


@pg.production(
    "bracket_definition : left_bracket attribute_definition multiple_attribute_definition right_bracket"
)
def bracket_definition(state, exp):
    return Bracket(filter(lambda ep: not isinstance(ep, LambdaBox), exp[1:-1]))


@pg.production(
    "multiple_bracket_definition : bracket_definition multiple_bracket_definition"
)
def multiple_bracket_definition(state, exp):
    return MultipleBracket(
        filter(lambda ep: not isinstance(ep, LambdaBox), exp)
    )

@pg.production('tag_name : SELF_TAG')
@pg.production('tag_name : TAG')
def tag_name(state, exp):
    return TagName(exp[0].getstr())


@pg.production('tag : tag_name')
def empty_tag(state, exp):
    """Tags with out attribute."""
    return EmptyTag(exp[0])

@pg.production("tag : tag_name bracket_definition")
def tag(state, exp):
    return Tag(*exp)


@pg.production('parentheses_tag : tag_name left_parentheses bracket_definition bracket_definition multiple_bracket_definition right_parentheses')
def parentheses_tag(state, exp):
    tag_name, lp, *attributes, rp = exp
    return ParenthesesTag(
        tag_name,
        filter(lambda ep: not isinstance(ep, LambdaBox), attributes)
    )

@pg.production('multiple_tag : tag multiple_tag')
@pg.production('multiple_tag : parentheses_tag multiple_tag')
def multiple_tag(state, exp):
    return MultipleTag(
        filter(lambda ep: not isinstance(ep, LambdaBox), exp)
    )

@pg.production('single_tag : tag')
@pg.production('single_tag : parentheses_tag')
def single_tag(state, exp):
    return exp[0]



parser = pg.build()
