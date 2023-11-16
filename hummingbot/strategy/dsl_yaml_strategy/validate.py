
import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML: {exc}")
        exit(1)

def validate_strategy(strategy):
    if not strategy.get('name'):
        return {"valid": False, "message": "Strategy name is missing"}
    if not strategy.get('version'):
        return {"valid": False, "message": "Strategy version is missing"}
    # Add more validation rules as needed
    return {"valid": True, "message": "Strategy is valid"}

def validate_market(market):
    if not market.get('connector'):
        return {"valid": False, "message": "Market connector is missing"}
    if not market.get('pairs'):
        return {"valid": False, "message": "Market pairs are missing"}
    # Add more validation rules as needed
    return {"valid": True, "message": "Market is valid"}

def main():
    yaml_data = load_yaml('strategy.yaml')

    # Validate strategy
    strategy_result = validate_strategy(yaml_data['strategy_model'])
    print(f"Strategy validation: {strategy_result['message']}")

    # Validate each market
    for market in yaml_data['strategy_model'].get('markets', []):
        market_result = validate_market(market)
        print(f"Market validation: {market_result['message']}")

if __name__ == '__main__':
    main()
