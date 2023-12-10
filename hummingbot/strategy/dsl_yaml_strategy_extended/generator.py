
import os
import jinja2
from validator import validate_strategy, load_yaml

def generate_script(strategy, template_dir='templates', output_dir='output'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    template = env.get_template('strategy_template.py.j2')

    script = template.render(strategy=strategy)

    output_path = os.path.join(output_dir, f"{strategy['name']}_strategy.py")
    try:
        with open(output_path, 'w') as file:
            file.write(script)
        print(f"Generated script saved to {output_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    yaml_data = load_yaml('yaml_files/strategy_2.yaml')
    strategy_result = validate_strategy(yaml_data['strategy_model'])

    if strategy_result['valid']:
        generate_script(yaml_data['strategy_model'])
    else:
        print(f"Validation failed: {strategy_result['message']}")

if __name__ == '__main__':
    main()
