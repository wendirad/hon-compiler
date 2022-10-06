
class Token:
    """
    A list of all token names, accepted by the parser.
    """

    LEFT_BRACE = r'\{'
    RIGHT_BRACE = r"\}"
    LEFT_BRACKET = r"\["
    RIGHT_BRACKET = r"\]"
    LEFT_PARA = r"\("
    RIGHT_PARA = r"\)"
    TAG = r"\[a-zA-Z0-9]+"
    COMMA = r","
    STRING = r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''
    VARIABLE = r"\:[a-zA-Z]\w+"
    ATTRIBUTE = r"[a-zA-Z]+(-[a-zA-Z]+)*"
    VAR_ACCESS = r"\%[a-zA-Z\_]+[a-zA-Z0-9\_]+"
    ASSIGN_OP = r"\="
