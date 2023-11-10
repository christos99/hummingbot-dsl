from lexer_dsl import lexer
from parser_dsl import parser
from synt_gram import correct_syntax_tests, error_handling_tests

# Function to test lexer and parser in sequence
def run_pipeline_tests(test_cases, lexer, parser):
    for test in test_cases:
        print(f"\nTesting input string: {test}")

        # Test the lexer
        print("Lexer output:")
        lexer.input(test)
        try:
            while True:
                tok = lexer.token()
                if not tok:
                    break  # No more input
                print(tok)
        except SyntaxError as se:
            print(f"Syntax error in lexer: {se}")
            continue  # Skip to the next test case
        except Exception as e:
            print(f"Unexpected error in lexer: {e}")
            continue  # Skip to the next test case

        # Test the parser
        print("Parser output:")
        try:
            result = parser.parse(test)
            print(f"The string '{test}' is parsed as {result}.")
        except SyntaxError as e:
            print(f"Syntax error in parser! {e}")
        except Exception as e:
            print(f"Unexpected error in parser: {e}")

# Execute the tests
run_pipeline_tests(error_handling_tests, lexer, parser)
