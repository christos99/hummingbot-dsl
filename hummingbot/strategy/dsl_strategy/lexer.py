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

# Regular expression rules for simple tokens
t_BUY = r'BUY'
t_SELL = r'SELL'
t_IF = r'IF'
t_PRICE = r'[Pp][Rr][Ii][Cc][Ee]'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'=='
t_LE = r'<='
t_GE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SMA = r'SMA'
t_EMA = r'EMA'
t_RSI = r'RSI'
t_CROSSOVER = r'[Cc][Rr][Oo][Ss][Ss][Oo][Vv][Ee][Rr]'
t_VOLUME = r'[Vv][Oo][Ll][Uu][Mm][Ee]'
t_BALANCE = r'[Bb][Aa][Ll][Aa][Nn][Cc][Ee]'
t_COMMA = r','


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert string to a number
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Function to test the lexer
def tet(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


# # To test the lexer, remove the comments from the following lines and run this file.
# test_data = '''
# BUY IF price < SMA(50) AND VOLUME > 10000
# SELL IF PRICE > SMA(50) AND RSI(14) > 70
# '''
# tet(test_data)
