# Assume we have a file named lexer_dsl.py which contains a lexer instance
from lexer_dsl import lexer
from parser_dsl import parser

# Correct Syntax Test Cases
correct_syntax_tests = [
    "BUY IF PRICE < 100",
    "SELL IF PRICE > 150",
    "BUY IF PRICE > 100 AND VOLUME < 50000",
    "SELL IF PRICE <= 200 OR VOLUME > 100000",
    "BUY IF NOT PRICE == 300",
    "SELL IF (PRICE < 100 AND VOLUME > 1000) OR BALANCE > 5000",
    "BUY IF PRICE > 50 AND PRICE < 100 AND PRICE <= 200 AND PRICE >= 150 AND PRICE == 175",
    "BUY IF CROSSOVER(SMA(30), PRICE) AND RSI(14) < 30",
    "SELL IF PRICE > EMA(14) AND RSI(14) > 70",
    "BUY IF VOLUME > 10000 AND BALANCE < 1000",
    "SELL IF (PRICE < SMA(50) OR PRICE < EMA(50)) AND VOLUME > 10000 OR BALANCE < 500",
]

# Error Handling Test Cases
error_handling_tests = [
    "BUY IF PRICE ??? 100",
    "SELL IF VOLUME >",
    "BUY PRICE < 100",
    "BUY IF (PRICE < 100 AND VOLUME > 5000",
    "SELL IF PRICE > (100 AND VOLUME < 20000)",
    "BUY IF PRICE < 10k",
    "BUY IF PRICE >< 200",
    "SELL 100 SHARES",
    "BUY IF AND PRICE > 100",
    "IF BUY PRICE < 100",
]


# Lexer test execution function
def run_lexer_tests(test_cases, lexer):
    for test in test_cases:
        lexer.input(test)
        print(f"Testing: {test}")
        try:
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No more input
                print(tok)
        except SyntaxError as se:
            print(f"Syntax error: {se}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Test the parser
def demo_parser(input_string):
    try:
        result = parser.parse(input_string)
        print(f"The string '{input_string}' is parsed as {result}.")
    except SyntaxError as e:
        print(f"Syntax error in input! {e}")

# Now execute the lexer test cases
# run_lexer_tests(correct_syntax_tests, lexer)
for test_string in correct_syntax_tests:
    demo_parser(test_string)


# run_lexer_tests(error_handling_tests, lexer)
