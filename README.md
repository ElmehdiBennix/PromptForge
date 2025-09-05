# PromptForge: A System for Dynamic AI Agent Instruction Management

## 🎯 Overview

This repository provides a comprehensive framework for forging and managing system instructions for AI agents. In modern development, using AI agents across different tools (like VS Code, Gemini CLI, etc.) often leads to inconsistent behavior and a loss of context when switching between projects.

`PromptForge` solves this by offering a centralized system to create, customize, and deploy tailored instructions for any workflow. It enables dynamic, context-aware instruction generation, ensuring that your AI agent always operates with the correct persona, rules, and project-specific knowledge.

## ✨ Key Features

*   **⚙️ Centralized Instruction Generator:** A powerful Python script to craft detailed system instructions from templates.
*   **🔌 Workflow-Specific Templates:** Includes ready-to-use templates for VS Code (`copilot-instructions.md`) and Gemini CLI (`GEMINI.md`).
*   **🔄 Dynamic Context Switching:** AI agents automatically load the correct generated instructions from the project directory you are in.
*   **🧩 Extensible & Modular:** Easily extend the system with new templates for future AI agents and workflows.

## 🚀 Getting Started

### Prerequisites

*   Python 3.6+

### Usage

The core of this project is the `generate.py` script. It takes a template file, applies your project-specific details, and generates a final instruction file.

1.  **Choose a template** from the `/templates` directory.
2.  **Run the script** with your project details.

**Example:**

```bash
python3 src/generate.py \
    --template templates/gemini_cli.md.template \
    --output ./examples/my-awesome-app/GEMINI.md \
    --project-name "My Awesome App" \
    --technologies "React, Node.js, PostgreSQL" \
    --style-guide "Prettier for JS, PEP8 for Python" \
    --testing-framework "Jest" \
    --rules "- Do not add new dependencies without approval.\n- All components must have tests."
```

This command will create a GEMINI.md file in the example directory, populated with the details you provided.
📁 Project Structure
```
/PromptForge
|-- /src                    # Core generator scripts
|   |-- generate.py
|-- /templates              # Instruction templates with placeholders
|   |-- vscode_copilot_instructions.md.template
|   |-- gemini_cli.md.template
|-- /examples               # Example generated output files
|   |-- my-awesome-app/
|-- .gitignore
|-- README.md
|-- GEMINI.md               # Instructions for this project itself
```
