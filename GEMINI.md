# Gemini CLI Instructions for PromptForge

## Project Overview

This project, "PromptForge," is a Python-based framework for generating system instructions for AI agents. Its goal is to standardize and streamline the way developers provide context to AI tools like Gemini CLI and VS Code Copilot.

## Technologies

*   **Language:** Python 3
*   **Core Libraries:** `argparse` (standard library)
*   **Development Style:** Procedural scripting. The code should be simple, readable, and have minimal dependencies.

## Key Files

*   `src/generate.py`: The main script that performs the template-to-instruction generation.
*   `templates/`: Directory containing instruction templates with `{{PLACEHOLDER}}` syntax.

## Commands

*   To run the generator: `python3 src/generate.py --template <template_path> --output <output_path> [options]`
*   To see available options: `python3 src/generate.py --help`

## Rules and Constraints

1.  **Simplicity First:** When modifying the `generate.py` script, do not add external libraries. Stick to the Python standard library.
2.  **Template Syntax:** All new templates must use the `{{VARIABLE_NAME}}` syntax for placeholders.
3.  **Clarity in Documentation:** When adding new features, update the main `README.md` with clear usage instructions.
