
import yaml

class Strategy:
    def __init__(self, name, version, type, markets, parameters):
        self.name = name
        self.version = version
        self.type = type
        self.markets = markets
        self.parameters = parameters

    # Add methods to process the strategy

class Market:
    def __init__(self, connector, pairs):
        self.connector = connector
        self.pairs = pairs

    # Add methods specific to Market

class Parameter:
    def __init__(self, name, type, default):
        self.name = name
        self.type = type
        self.default = default

    # Add methods specific to Parameter

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

def parse_strategy(data):
    if 'markets' in data and 'parameters' in data:
        markets = [Market(m['connector'], m['pairs']) for m in data['markets']]
        parameters = [Parameter(p['name'], p['type'], p['default']) for p in data['parameters']]
        return Strategy(data['name'], data['version'], data['type'], markets, parameters)
    else:
        print("Invalid strategy data format")
        exit(1)

def main():
    yaml_data = load_yaml('strategy.yaml')
    strategy = parse_strategy(yaml_data['strategy_model'])
    # Process the strategy object as needed

if __name__ == '__main__':
    main()
