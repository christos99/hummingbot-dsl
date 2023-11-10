# Correct Syntax Test Cases
correct_syntax_tests = [
    # "BUY IF PRICE < 100",
    # "SELL IF PRICE > 150",
    # "BUY IF PRICE > 100 AND VOLUME < 50000",
    # "SELL IF PRICE <= 200 OR VOLUME > 100000",
    # "BUY IF NOT PRICE == 300",
    # "BUY IF PRICE > 50 AND PRICE < 100 AND PRICE <= 200 AND PRICE >= 150 AND PRICE == 175",
    # "BUY IF VOLUME > 10000 AND BALANCE < 1000",
    # "SELL IF ( PRICE < 100 AND VOLUME > 1000 ) OR BALANCE > 5000",
    # "BUY IF CROSSOVER(SMA(30), PRICE) AND RSI(14) < 30",
    # "SELL IF PRICE > EMA(14) AND RSI(14) > 70",
    # "SELL IF (PRICE < SMA(50) OR PRICE < EMA(50)) AND VOLUME > 10000 OR BALANCE < 500",
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
