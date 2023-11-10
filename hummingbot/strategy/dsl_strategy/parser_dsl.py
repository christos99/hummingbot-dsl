from ply import yacc

# Assuming your lexer tokens are defined and imported correctly
# from your lexer file, something like this:
from lexer_dsl import tokens

# Define the precedence level and associativity of operators
precedence = (
    ('nonassoc', 'BUY', 'SELL'),
    ('nonassoc', 'IF'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'EQ', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'CROSSOVER', 'SMA', 'EMA', 'RSI')
)

# The very basic rule that forms a command (e.g., BUY IF condition, SELL IF condition)
def p_command(p):
    """command : BUY IF condition
               | SELL IF condition"""
    p[0] = (p[1], p[3])

# Parsing conditions
def p_condition(p):
    '''condition : expression
                 | NOT condition
                 | condition AND condition
                 | condition OR condition'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == 'NOT':
        p[0] = ('NOT', p[2])
    elif p[2] == 'AND':
        p[0] = ('AND', p[1], p[3])
    elif p[2] == 'OR':
        p[0] = ('OR', p[1], p[3])

# Parsing expressions enclosed in parentheses
def p_expression_group(p):
    """expression : LPAREN condition RPAREN"""
    p[0] = p[2]

# Expressions
def p_expression(p):
    '''expression : PRICE
                  | VOLUME
                  | BALANCE
                  | NUMBER
                  | function_call
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression'''
    if len(p) == 2:
        p[0] = ('PRICE', 'PRICE') if p[1] == 'PRICE' else ('VOLUME', 'VOLUME') if p[1] == 'VOLUME' else ('BALANCE', 'BALANCE') if p[1] == 'BALANCE' else ('NUMBER', p[1])
    else:
        p[0] = (p[2], p[1], p[3])



# Handling function calls
def p_function_call(p):
    """function_call : CROSSOVER LPAREN expression COMMA expression RPAREN
                     | SMA LPAREN NUMBER RPAREN
                     | EMA LPAREN NUMBER RPAREN
                     | RSI LPAREN NUMBER RPAREN"""
    if p[1] == 'CROSSOVER':
        p[0] = ('CROSSOVER', p[3], p[5])
    elif p[1] in ['SMA', 'EMA', 'RSI']:
        p[0] = (p[1], p[3])



# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token [{p.type}] -> [{p.value}], on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc(debug=True)

# Example of how to use the parser with some input
def parse_input(input_string):
    try:
        result = parser.parse(input_string)
        print(result)
    except Exception as e:
        print(e)

# # Test the parser
test_strings = [
    "BUY IF PRICE < 100",
    "SELL IF PRICE > 150 AND VOLUME < 50000",
    "SELL IF ( PRICE < 100 AND VOLUME > 1000 )",
    # Add more test strings as needed
]

for test_string in test_strings:
    parse_input(test_string)
