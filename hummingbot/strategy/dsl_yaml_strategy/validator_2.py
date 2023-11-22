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
    required_fields = ['name', 'version', 'type', 'author', 'author_email', 'description', 'labels', 'markets']
    for field in required_fields:
        if not strategy.get(field):
            return {"valid": False, "message": f"Strategy {field} is missing"}

    # Validate strategy type
    valid_types = ['StrategyBase', 'Script', 'PMM', 'LM']
    if strategy['type'] not in valid_types:
        return {"valid": False, "message": f"Invalid strategy type: {strategy['type']}"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Strategy is valid"}



def validate_market(market):
    if not market.get('connector'):
        return {"valid": False, "message": "Market connector is missing"}
    valid_connectors = ['binance', 'kucoin', 'ascent_ex', 'gate_io']
    if market['connector'] not in valid_connectors:
        return {"valid": False, "message": f"Invalid market connector: {market['connector']}"}

    if not market.get('pairs'):
        return {"valid": False, "message": "Market pairs are missing"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Market is valid"}

def validate_parameter(parameter):
    required_fields = ['name', 'type', 'description', 'prompt_msg', 'default', 'keyword', 'dynamic_reconfigure', 'prompt_on_new']
    for field in required_fields:
        if field not in parameter:
            return {"valid": False, "message": f"Parameter {field} is missing"}

    valid_types = ['int', 'float', 'str', 'bool', 'list', 'dict']
    if parameter['type'] not in valid_types:
        return {"valid": False, "message": f"Invalid parameter type: {parameter['type']}"}

    # Add more specific validations as needed
    return {"valid": True, "message": "Parameter is valid"}


def main():
    yaml_data = load_yaml('strategy_2.yaml')

    # Validate strategy
    strategy_result = validate_strategy(yaml_data['strategy_model'])
    print(f"Strategy validation: {strategy_result['message']}")

    # Validate each market
    for market in yaml_data['strategy_model'].get('markets', []):
        market_result = validate_market(market['market'])
        print(f"Market validation: {market_result['message']}")

    # Validate each parameter
    for parameter in yaml_data['strategy_model'].get('parameters', []):
        parameter_result = validate_parameter(parameter['parameter'])
        print(f"Parameter validation: {parameter_result['message']}")

if __name__ == '__main__':
    main()


