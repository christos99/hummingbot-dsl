# Assume we have a file named lexer_dsl.py which contains a lexer instance
from lexer_dsl import lexer
from parser_dsl import parser
from synt_gram import correct_syntax_tests, error_handling_tests


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
