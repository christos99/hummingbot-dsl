# parser.py

from ply import yacc

# Import tokens from lexer
from hummingbot.strategy.dsl_strategy.lexer import tokens


# This function is for strategy parsing.
def p_strategy(p):
    """strategy : buy_strategy
                | sell_strategy
                | conditional_strategy"""
    p[0] = p[1]


def p_buy_strategy(p):
    """buy_strategy : BUY IF simple_condition"""
    p[0] = ('BUY', p[3])


def p_sell_strategy(p):
    """sell_strategy : SELL IF simple_condition"""
    p[0] = ('SELL', p[3])


def p_conditional_strategy(p):
    """conditional_strategy : IF compound_condition"""
    p[0] = ('CONDITION', p[2])


def p_compound_condition(p):
    """compound_condition : simple_condition AND simple_condition
                          | simple_condition OR simple_condition
                          | NOT simple_condition
                          | LPAREN compound_condition RPAREN"""
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif p[1] == 'NOT':
        p[0] = ('NOT', p[2])
    else:
        p[0] = p[2]


def p_simple_condition(p):
    """simple_condition : PRICE comparison NUMBER
                        | VOLUME comparison NUMBER"""
    p[0] = (p[2], p[1], p[3])


def p_comparison(p):
    """comparison : LT
                  | GT
                  | LE
                  | GE
                  | EQ"""
    p[0] = p[1]


# We'll need to expand on the above grammar to add more conditions and features, but this should address the infinite recursion error.

# ... continue with the rest of the parser rules ...

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


# To test the parser, use the below function
def parse(data):
    result = parser.parse(data)
    return result


# Test the parser
test_data = "BUY IF PRICE < 100"
print(parse(test_data))
