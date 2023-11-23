import yaml

class Strategy:
    def __init__(self, name, version, type, markets, parameters):
        self.name = name
        self.version = version
        self.type = type
        self.markets = markets
        self.parameters = parameters

    def display(self):
        print(f"Strategy: {self.name}, Version: {self.version}, Type: {self.type}")
        for market in self.markets:
            market.display()
        for parameter in self.parameters:
            parameter.display()

class Market:
    def __init__(self, connector, pairs):
        self.connector = connector
        self.pairs = pairs

    def display(self):
        print(f"Market: {self.connector}, Pairs: {self.pairs}")

class Parameter:
    def __init__(self, name, type, default):
        self.name = name
        self.type = type
        self.default = default

    def display(self):
        print(f"Parameter: {self.name}, Type: {self.type}, Default: {self.default}")

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML: {exc}")
        return None

def parse_strategy(data):
    if not data or 'markets' not in data or 'parameters' not in data:
        print("Invalid strategy data format")
        return None

    markets = [Market(m['connector'], m['pairs']) for m in data['markets']]
    parameters = [Parameter(p['name'], p['type'], p['default']) for p in data['parameters']]
    return Strategy(data['name'], data['version'], data['type'], markets, parameters)

def main():
    yaml_data = load_yaml('strategy.yaml')  # Adjust the file name as needed
    if yaml_data:
        strategy = parse_strategy(yaml_data['strategy_model'])
        if strategy:
            strategy.display()

if __name__ == '__main__':
    main()
