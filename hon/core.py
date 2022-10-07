from rply import LexerGenerator, ParserGenerator

from hon.constants import Token

lexer_generator = LexerGenerator()

lexer_generator.add("LEFT_BRACE", Token.LEFT_BRACE)
lexer_generator.add("RIGHT_BRACE", Token.RIGHT_BRACE)
lexer_generator.add("LEFT_BRACKET", Token.LEFT_BRACKET)
lexer_generator.add("RIGHT_BRACKET", Token.RIGHT_BRACKET)
lexer_generator.add("LEFT_PARA", Token.LEFT_PARA)
lexer_generator.add("RIGHT_PARA", Token.RIGHT_PARA)
lexer_generator.add("SELF_TAG", Token.SELF_TAG)
lexer_generator.add("TAG", Token.TAG)
lexer_generator.add("COMMA", Token.COMMA)
lexer_generator.add("STRING", Token.STRING)
lexer_generator.add("VARIABLE", Token.VARIABLE)
lexer_generator.add("ATTRIBUTE", Token.ATTRIBUTE)
lexer_generator.add("VAR_ACCESS", Token.VAR_ACCESS)
lexer_generator.add("ASSIGNMENT_OPERATOR", Token.ASSIGN_OP)

lexer_generator.ignore(r"\s+")

lexer = lexer_generator.build()

pg = ParserGenerator(
    [
        "LEFT_BRACE",
        "RIGHT_BRACE",
        "LEFT_BRACKET",
        "RIGHT_BRACKET",
        "LEFT_PARA",
        "RIGHT_PARA",
        "SELF_TAG",
        "TAG",
        "COMMA",
        "STRING",
        "VARIABLE",
        "VAR_ACCESS",
        "ATTRIBUTE",
        "ASSIGNMENT_OPERATOR",
    ],
    precedence=[
        ("left", ["SELF_TAG"]),
        ("left", ["TAG"]),
    ],
)
