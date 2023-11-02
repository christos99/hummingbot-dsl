from ply import lex

# List of token names. This is always required
tokens = (
   'BUY',
   'SELL',
   'IF',
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
   'PRICE',
   'VOLUME',
   'BALANCE',
   'NUMBER',
   'COMMA'
)

# Regular expression rules for simple tokens
t_BUY = r'BUY'
t_SELL = r'SELL'
t_IF = r'IF'
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
t_CROSSOVER = r'CROSSOVER'
t_PRICE = r'price'
t_VOLUME = r'volume'
t_BALANCE = r'balance'
t_COMMA = r','

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    # Convert string to a number
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
BUY IF price < SMA(50) AND volume > 10000
SELL IF price > SMA(50) AND RSI(14) > 70
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

