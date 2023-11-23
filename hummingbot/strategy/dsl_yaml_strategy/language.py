import yaml

class Strategy:
    def __init__(self, name, version, type, author, author_email, description, labels, markets, parameters):
        self.name = name
        self.version = version
        self.type = type
        self.author = author
        self.author_email = author_email
        self.description = description
        self.labels = labels
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
    def __init__(self, name, type, description, prompt_msg, default, keyword, dynamic_reconfigure, prompt_on_new):
        self.name = name
        self.type = type
        self.description = description
        self.prompt_msg = prompt_msg
        self.default = default
        self.keyword = keyword
        self.dynamic_reconfigure = dynamic_reconfigure
        self.prompt_on_new = prompt_on_new

    def display(self):
        print(f"Parameter: {self.name}, Type: {self.type}, Default: {self.default}")

class ExchangeConfig:
    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret

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
    if not data:
        print("Invalid strategy data format")
        return None

    markets = [Market(m['market']['connector'], m['market']['pairs']) for m in data.get('markets', [])]
    parameters = [Parameter(p['parameter']['name'], p['parameter']['type'], p['parameter']['description'], p['parameter']['prompt_msg'], p['parameter']['default'], p['parameter']['keyword'], p['parameter']['dynamic_reconfigure'], p['parameter']['prompt_on_new']) for p in data.get('parameters', [])]

    return Strategy(data['name'], data['version'], data['type'], data.get('author', ''), data.get('author_email', ''), data.get('description', ''), data.get('labels', []), markets, parameters)

def main():
    yaml_data = load_yaml('/Users/christos/hummingbot-dsl/hummingbot/strategy/dsl_yaml_strategy/demo_strategy.yaml')  # Replace with your actual file path
    if yaml_data:
        strategy = parse_strategy(yaml_data['strategy_model'])
        if strategy:
            strategy.display()  # Replace with your desired processing or output format

if __name__ == '__main__':
    main()
