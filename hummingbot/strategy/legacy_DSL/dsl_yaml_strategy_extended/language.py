import yaml
import argparse

class Strategy:
    def __init__(self, name, version, type, author, author_email, description, labels, markets, parameters):

        self.name = name

        # Attempt to convert 'version' to a float
        try:
            self.version = float(version)
        except ValueError:
            raise ValueError("Version must be a number that can be converted to float")

        # Define valid types and check (case-insensitive comparison)
        valid_types = {
            'strategybase': 'StrategyBase',
            'script': 'Script',
            'pmm': 'PMM',
            'lm': 'LM'
        }

        if type.lower() not in valid_types:
            valid_types_str = ", ".join(valid_types.values())  # Get the correct forms
            raise ValueError(f"Invalid strategy type '{type}'. Valid types are: {valid_types_str}")

        self.type = valid_types[type.lower()]  # Use the correct form of the recognized strategy type

        # Capitalize the first letter of each word in 'author'
        self.author = author.title()

        self.author_email = author_email
        self.description = description
        self.labels = labels
        self.markets = markets
        self.parameters = parameters

    def display(self):
        print(
            f"Strategy: {self.name}, Version: {self.version}, Type: {self.type}, Author: {self.author}, Email: {self.author_email}")
        print(f"Description: {self.description}")
        print("Labels: " + ", ".join(self.labels))
        for market in self.markets:
            market.display()
        for parameter in self.parameters:
            parameter.display()

    def to_dict(self):
        return {
            'name': self.name,
            'version': self.version,
            'type': self.type,
            'author': self.author,
            'author_email': self.author_email,
            'description': self.description,
            'labels': self.labels,
            'markets': [market.to_dict() for market in self.markets],
            'parameters': [parameter.to_dict() for parameter in self.parameters]
        }


class Market:
    def __init__(self, connector, pairs):
        self.connector = connector[0:].lower()
        self.pairs = [pair.upper() for pair in pairs]

    def display(self):
        print(f"Market: {self.connector[0].upper() + self.connector[1:].lower()}, Pairs: {', '.join(self.pairs)}")

    def to_dict(self):
        return {
            'connector': self.connector,
            'pairs': self.pairs
        }


class Parameter:
    def __init__(self, name, type, description, prompt_msg, default, keyword, dynamic_reconfigure, prompt_on_new):
        self.name = name
        self.type = self._convert_type(type)
        self.description = description
        self.prompt_msg = prompt_msg
        self.default = default
        self.keyword = keyword
        self.dynamic_reconfigure = self._convert_to_boolean(dynamic_reconfigure)
        self.prompt_on_new = self._convert_to_boolean(prompt_on_new)

    @staticmethod
    def _convert_type(type):
        if type == 'decimal':
            return 'float'
        return type

    @staticmethod
    def _convert_to_boolean(value):
        # If the value is None (parameter is missing), return None or a default value
        if value is None:
            return False  # or return False if you want to default to False

        # Convert different string capitalizations to boolean
        if isinstance(value, str):
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            else:
                raise ValueError("Value must be a boolean (true/false)")
        elif isinstance(value, bool):
            return value
        else:
            raise ValueError("Value must be a boolean (True/False)")

    def display(self):
        print(
            f"Parameter: {self.name}, Type: {self.type}, Description: {self.description}, Default: {self.default}, Keyword: {self.keyword}, Dynamic Reconfigure: {self.dynamic_reconfigure}, Prompt on New: {self.prompt_on_new}")

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'prompt_msg': self.prompt_msg,
            'default': self.default,
            'keyword': self.keyword,
            'dynamic_reconfigure': self.dynamic_reconfigure,
            'prompt_on_new': self.prompt_on_new
        }

class ExchangeConfig:
    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret

    def display(self):
        print(f"Exchange API Key: {self.apiKey}, Secret: {self.apiSecret}")

    def to_dict(self):
        return {
            'apiKey': self.apiKey,
            'apiSecret': self.apiSecret
        }


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

    # Handle missing 'markets' and 'parameters' keys
    markets_data = data.get('markets', [])
    parameters_data = data.get('parameters', [])

    markets = [Market(m.get('market', {}).get('connector', None), m.get('market', {}).get('pairs', [])) for m in markets_data]
    parameters = [Parameter(
        p.get('parameter', {}).get('name', None),
        p.get('parameter', {}).get('type', None),
        p.get('parameter', {}).get('description', None),
        p.get('parameter', {}).get('prompt_msg', None),
        p.get('parameter', {}).get('default', None),
        p.get('parameter', {}).get('keyword', None),
        p.get('parameter', {}).get('dynamic_reconfigure', None),
        p.get('parameter', {}).get('prompt_on_new', None)
    ) for p in parameters_data]

    return Strategy(
        data.get('name', None),
        data.get('version', None),
        data.get('type', None),
        data.get('author', ''),
        data.get('author_email', ''),
        data.get('description', ''),
        data.get('labels', []),
        markets,
        parameters
    )


def main(file_path):
    yaml_data = load_yaml(file_path)
    if yaml_data:
        strategy = parse_strategy(yaml_data['strategy_model'])
        if strategy:
            strategy.display()  # Display the parsed strategy
            return strategy
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse a strategy YAML file")
    parser.add_argument('file_path', help="Path to the strategy YAML file")
    args = parser.parse_args()

    strategy = main(args.file_path)
    if strategy:
        strategy.display()  # Optional additional display

