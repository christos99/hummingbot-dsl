import ply.lex as lex
from hummingbot.strategy.dsl_strategy.lexer import lexer
# Assuming you have a lexer object defined in your module

def test_lexer():
    def run_test(input_string):
        lexer.input(input_string)
        result = []

        while True:
            tok = lexer.token()
            if not tok:
                break
            result.append((tok.type, tok.value, tok.lineno, tok.lexpos))

        return result

    # Sample inputs and expected outputs
    tests = {
        "BUY IF price < SMA(50)": [('BUY', 'BUY', 1, 0), ('IF', 'IF', 1, 4), ('PRICE', 'price', 1, 7), ('LT', '<', 1, 13), ('SMA', 'SMA', 1, 15), ('LPAREN', '(', 1, 18), ('NUMBER', 50, 1, 19), ('RPAREN', ')', 1, 21)],
        # Add more sample inputs and their expected token sequences
    }

    for input_string, expected_tokens in tests.items():
        assert run_test(input_string) == expected_tokens
