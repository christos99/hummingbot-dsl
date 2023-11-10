from lexer_dsl import lexer
from parser_dsl import parser
from synt_gram import correct_syntax_tests, error_handling_tests

def get_astree(tests):
    ast_trees = []
    for input_string in tests:
        try:
            if not isinstance(input_string, str):
                raise ValueError(f"Expected a string, but got {type(input_string)}")

            # Reset lexer to initial state before processing new input
            lexer.lineno = 1
            lexer.input(input_string)

            # Parse the input string to produce the AST
            ast = parser.parse(input_string, lexer=lexer)
            ast_trees.append(ast)
        except Exception as e:
            print(f"Error processing input: '{input_string}'")
            print(e)
            ast_trees.append(None)  # Append None or some error indicator
    return ast_trees

# Use the function to get ASTs for the test strings
ast_trees = get_astree(correct_syntax_tests)
for ast in ast_trees:
    print(ast)  # Print the AST for each input string
