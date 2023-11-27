import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Import the validator function from validator.py (assuming it's refactored into a callable function)
from validator import main as validate_and_save_strategy


def generate_script(file_path):
    # Validate the strategy and get the path of the validated file
    validated_file_path = validate_and_save_strategy(file_path)
    if not validated_file_path:
        print("Validation failed. Script generation aborted.")
        return

    # Load strategy data from the YAML file
    with open(validated_file_path, 'r') as file:
        strategy_data = yaml.safe_load(file)['strategy_model']

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('./templates'))  # Template in current directory
    template = env.get_template('strategy_template.j2')

    # Render the template with strategy data
    rendered_script = template.render(strategy=strategy_data)

    # Output or save the rendered script
    print(rendered_script)

    # Determine output file path
    base_name = os.path.basename(validated_file_path).rsplit('.', 1)[0]
    output_file_path = f"{base_name}_script.py"

    # Write to a file with the new name
    with open(f'output_strategies/{output_file_path}', 'w') as file:
        file.write(rendered_script)


if __name__ == "__main__":
    input_file_path = '/Users/christos/hummingbot-dsl/hummingbot/strategy/dsl_yaml_strategy/yaml_files/demo_strategy.yaml'
    generate_script(input_file_path)
