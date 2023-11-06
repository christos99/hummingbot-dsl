# Hummingbot DSL PoC

## Introduction
Welcome to the Hummingbot DSL (Domain-Specific Language) Proof of Concept! This project aims to explore the feasibility and utility of a bespoke DSL for [Hummingbot](https://github.com/hummingbot/hummingbot), an open-source cryptocurrency trading bot framework. The purpose of this DSL is to simplify the creation, modification, and sharing of trading strategies within the Hummingbot community.

## Project Goals
The PoC for the Hummingbot DSL aims to:
- Provide an intuitive syntax for expressing trading strategies.
- Facilitate easy customization and extension of Hummingbot's capabilities.
- Enhance readability and maintainability of trading algorithms.
- Enable traders to write less boilerplate code for complex strategies.
- Validate the concept with a subset of Hummingbot's functionality.

## Scope of PoC
In this PoC, we focus on the following aspects:
- Syntax design that reflects common trading operations and strategy paradigms.
- A parser that translates DSL scripts into executable code compatible with Hummingbot.
- Basic backtesting functionality to demonstrate the DSL's capability.
- A set of example strategies that highlight the DSL's expressiveness.

## Getting Started
To get started with the Hummingbot DSL PoC:

1. Clone this repository.

2. Navigate to the repository directory.

3. Follow the setup instructions in the `INSTALL.md` to set up your development environment.

4. Explore the `dsl_strategy` directory to see sample DSL scripts.

5. Run a sample script to see it in action (detailed instructions in `[not_yet_defined].md`).

## Usage Example
Here's a sneak peek at what a Hummingbot DSL script might look like:
```dsl
strategy MyFirstStrategy {
 market: "binance/BTC-USDT"
 entry: {
     condition: price_above(20000)
     action: buy(1 BTC)
 }
 exit: {
     condition: profit_above(10%)
     action: sell(100% position)
 }
}

