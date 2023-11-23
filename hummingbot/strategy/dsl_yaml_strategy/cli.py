
import argparse
import yaml
import sys
import os
import tempfile

temp_file_path = os.path.join(tempfile.gettempdir(), "temp_strategy.yaml")

def load_strategy(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(f"Error loading YAML file: {exc}")
        sys.exit(1)

def save_strategy(file_path):
    if os.path.exists(temp_file_path):
        with open(temp_file_path, 'r') as file:
            strategy = yaml.safe_load(file)
        with open(file_path, 'w') as file:
            yaml.dump(strategy, file)
        os.remove(temp_file_path)
        print(f"Strategy saved to {file_path}")
    else:
        print("No strategy created. Use 'create' first.")

def create_strategy():
    strategy = {
        'strategy_model': {
            'name': input("Enter strategy name: "),
            'version': input("Enter strategy version: "),
            'type': input("Enter strategy type (StrategyBase | Script | PMM | LM): "),
            'author': input("Enter author name: "),
            'author_email': input("Enter author email: "),
            'description': input("Enter description: "),
            'labels': input("Enter labels (comma-separated): ").split(','),
            'markets': [],
            'parameters': []
        }
    }

    # Adding markets
    while True:
        add_market = input("Do you want to add a market? (yes/no): ")
        if add_market.lower() != 'yes':
            break
        market = {
            'market': {
                'connector': input("Enter connector (binance | kucoin | ascent_ex | gate_io): "),
                'pairs': input("Enter pairs (comma-separated): ").split(',')
            }
        }
        strategy['strategy_model']['markets'].append(market)

    # Adding parameters
    while True:
        add_param = input("Do you want to add a parameter? (yes/no): ")
        if add_param.lower() != 'yes':
            break
        parameter = {
            'parameter': {
                'name': input("Enter parameter name: "),
                'type': input("Enter parameter type (int | float | str | bool | list | dict): "),
                'description': input("Enter description: "),
                'prompt_msg': input("Enter prompt message: "),
                'default': input("Enter default value: "),
                'keyword': input("Enter keyword: "),
                'dynamic_reconfigure': input("Is dynamic reconfigure? (true | false): ").lower() == 'true',
                'prompt_on_new': input("Prompt on new? (true | false): ").lower() == 'true'
            }
        }
        strategy['strategy_model']['parameters'].append(parameter)

    with open(temp_file_path, 'w') as file:
        yaml.dump(strategy, file)
    return strategy

def main():
    parser = argparse.ArgumentParser(description='Strategy YAML CLI')
    parser.add_argument('action', choices=['load', 'create', 'save'], help='Action to perform')
    parser.add_argument('-f', '--file', help='Path to the YAML file', required=False)
    args = parser.parse_args()

    if args.action == 'load':
        if args.file:
            strategy = load_strategy(args.file)
            print(strategy)
        else:
            print("Please specify a file path with -f or --file")
    elif args.action == 'create':
        strategy = create_strategy()
        print("Strategy created. Use 'save' action to save it to a file.")
        print(strategy)
    elif args.action == 'save':
        if args.file:
            if temp_strategy is None:
                print("No strategy created. Use 'create' first.")
                return
            save_strategy(args.file, temp_strategy)
            print(f"Strategy saved to {args.file}")
            temp_strategy = None  # Clear the temporary storage
        else:
            print("Please specify a file path with -f or --file")

if __name__ == '__main__':
    main()
