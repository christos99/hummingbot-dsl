import re
from ply import lex


# List of token names. This is always required
tokens = (
    'BUY',
    'SELL',
    'IF',
    'PRICE',
    'AND',
    'OR',
    'NOT',
    'LT',
    'GT',
    'EQ',
    'LE',
    'GE',
    'LPAREN',
    'RPAREN',
    'SMA',
    'EMA',
    'RSI',
    'CROSSOVER',
    'VOLUME',
    'BALANCE',
    'NUMBER',
    'COMMA'
)

# Simple token regex rules
t_BUY = r'(?i)\bbuy\b'
t_SELL = r'(?i)\bsell\b'
t_IF = r'(?i)\bif\b'
t_PRICE = r'(?i)\bprice\b'
t_AND = r'(?i)\band\b'
t_OR = r'(?i)\bor\b'
t_NOT = r'(?i)\bnot\b'
t_SMA = r'(?i)\bsma\b'
t_EMA = r'(?i)\bema\b'
t_RSI = r'(?i)\brsi\b'
t_CROSSOVER = r'(?i)\bcrossover\b'
t_VOLUME = r'(?i)\bvolume\b'
t_BALANCE = r'(?i)\bbalance\b'
t_COMMA = r','

# Regular expressions for comparison operators using literals
literals = ['<', '>', '=', '+', '-', '*', '/']

# More complex token regex rules
def t_LE(t):
    r'<='
    return t

def t_GE(t):
    r'>='
    return t

def t_EQ(t):
    r'=='
    return t

def t_LT(t):
    r'<'
    return t

def t_GT(t):
    r'>'
    return t

def t_LPAREN(t):
    r"""\("""
    return t

def t_RPAREN(t):
    r"""\)"""
    return t

# Number TOKEN rule with conversion to integer
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)  # Convert string to a number (float if it contains a period)
    return t


# Rule for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    line_start = t.lexer.lexdata.rfind('\n', 0, t.lexer.lexpos) + 1
    column = (t.lexer.lexpos - line_start) + 1
    error_message = f"Illegal character '{t.value[0]}' at line {t.lexer.lineno} column {column}"
    raise SyntaxError(error_message)

# Build the lexer with re.IGNORECASE to match tokens case-insensitively
lexer = lex.lex(reflags=re.IGNORECASE)

