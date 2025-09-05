import argparse
import sys
import re

def generate_instruction(template_path, output_path, context):
    """
    Reads a template file, replaces placeholders with context values,
    and writes the result to an output file.

    Args:
        template_path (str): The path to the template file.
        output_path (str): The path to the output instruction file.
        context (dict): A dictionary of placeholder keys and their values.
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {template_path}", file=sys.stderr)
        sys.exit(1)

    # Replace placeholders in the format {{KEY}}
    # Using a function for replacement to handle missing keys gracefully
    def replace_func(match):
        key = match.group(1)
        return context.get(key, f"{{{{__{key}_UNDEFINED__}}}}")

    output_content = re.sub(r"{{\{{([a-zA-Z_]+)\}}}}", replace_func, template_content)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"Successfully generated instruction file at: {output_path}")
    except IOError as e:
        print(f"Error: Could not write to output file at {output_path}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to parse command-line arguments and run the generator.
    """
    parser = argparse.ArgumentParser(
        description="Generate system instruction files from templates.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--template", required=True, help="Path to the template file.")
    parser.add_argument("--output", required=True, help="Path for the generated output file.")
    parser.add_argument("--project-name", default="Unnamed Project", help="The name of the project.")
    parser.add_argument("--technologies", default="Not specified", help="Comma-separated list of technologies.")
    parser.add_argument("--style-guide", default="Not specified", help="The coding style guide.")
    parser.add_argument("--testing-framework", default="Not specified", help="The testing framework used.")
    parser.add_argument(
        "--rules",
        default="- Follow standard best practices.",
        help="Core rules for the AI agent. Use \n for new lines."
    )

    args = parser.parse_args()

    # Create context dictionary from arguments
    context = {
        'PROJECT_NAME': args.project_name,
        'TECHNOLOGIES': args.technologies,
        'STYLE_GUIDE': args.style_guide,
        'TESTING_FRAMEWORK': args.testing_framework,
        'RULES': args.rules.replace('\n', '\n'), # Handle newlines in rules
    }

    generate_instruction(args.template, args.output, context)

if __name__ == "__main__":
    main()
