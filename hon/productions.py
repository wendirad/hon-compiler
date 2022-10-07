from hon.baseboxs import *

from hon.core import pg

@pg.production('expression : attribute_definition')
def expression(state, exp):
    return exp[0]

@pg.production('left_brace : LEFT_BRACE')
def left_brace(state, exp):
    return LeftBrace(exp[0].getstr())

@pg.production('right_brace : RIGHT_BRACE')
def right_brace(state, exp):
    return RightBrace(exp[0].getstr())

@pg.production('left_bracket : LEFT_BRACKET')
def left_bracket(state, exp):
    return LeftBracket(exp[0].getstr())

@pg.production('right_bracket : RIGHT_BRACKET')
def right_bracket(state, exp):
    return RightBracket(exp[0].getstr())

@pg.production('left_parentheses : LEFT_PARA')
def left_parentheses(state, exp):
    return LeftParentheses(exp[0].getstr())

@pg.production('right_parentheses : RIGHT_PARA')
def right_parentheses(state, exp):
    return RightParentheses(exp[0].getstr())

@pg.production('comma : COMMA')
def right_parentheses(state, exp):
    return Comma(exp[0].getstr())

@pg.production('assignment_operator : ASSIGNMENT_OPERATOR')
def assignment_operator(state, exp):
    return AssignemntOperator(exp[0].getstr())

@pg.production('string : STRING')
def string(state, exp):
    return String(exp[0].getstr())

@pg.production('variable : VARIABLE')
def variable(state, exp):
    return Variable(exp[0].getstr())

@pg.production('attribute_name : ATTRIBUTE')
def attribute_name(state, exp):
    return AttributeName(exp[0].getstr())

@pg.production('attribute_definition : attribute_name assignment_operator string')
def attribute_definition(state, exp):
    return Attribute(*exp)

parser = pg.build()
