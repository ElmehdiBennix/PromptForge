# Project Architecture & Documentation

## 1. Project Overview

PromptForge is a command-line TUI application designed to help users generate structured system prompts for language models like Gemini. It interactively asks the user for an "expert" persona and a specific query, then constructs a detailed system prompt based on established best practices.

The target audience is developers, researchers, and prompt engineers who need to rapidly prototype and generate effective system prompts for various tasks.

## 2. Architecture Decisions

*   **Language/Framework:** Node.js with the `inquirer` library for interactive command-line prompts.
*   **Core Components:**
    *   **UI Layer (`src/ui`):** Handles all user interaction, primarily through `inquirer` prompts. It is responsible for gathering the necessary inputs from the user.
    *   **Business Logic (`src/core`):** Contains the core logic for generating the final system prompt based on the user's input.
    *   **Main (`src/main.js`):** The main application entry point that orchestrates the UI and core logic.
*   **State Management:** The application is stateless. Each run is independent and gathers all required information from the user at runtime.
*   **Error Handling Strategy:** Errors are handled via standard Node.js mechanisms (try-catch blocks). User input validation is managed by the `inquirer` library's validation features.
*   **TUI Design Philosophy:** The TUI is designed for clarity and efficiency, guiding the user through a simple, step-by-step process to generate the prompt.

## 3. Folder Structure

```
/PromptForge/
├── src/                      # Source code
│   ├── main.js               # Application entry point
│   ├── ui/                   # TUI components and views
│   │   └── prompt.js         # Logic for handling user prompts via inquirer
│   └── core/                 # Core business logic
│       └── engine.js         # Logic for generating the final system prompt
├── docs/                     # Documentation
│   └── gemini.md             # This documentation file
├── tests/                    # Unit and integration tests
├── .gitignore
├── package.json
├── LICENSE
└── README.md
```

## 4. TUI Feature Enhancements

The following TUI features are proposed to enhance the application's usability and power:

*   **Enhanced Input with Autocomplete/Suggestions:**
    *   **Description:** For the "expert" prompt, provide suggestions for common expert types (e.g., "Software Developer," "Chef," "Historian").
    *   **Rationale:** Speeds up user input and provides ideas for personas.
*   **Real-time Prompt Preview:**
    *   **Description:** After the user enters the expert and query, display the fully constructed system prompt for their review before finishing.
    *   **Rationale:** Provides immediate feedback and allows the user to verify the final output.
*   **Command History:**
    *   **Description:** Implement a mechanism to save and recall previous queries.
    *   **Rationale:** Improves efficiency for users who frequently reuse or modify previous queries.
*   **Multi-line Input for Queries:**
    *   **Description:** Use `inquirer`'s `editor` type for the query prompt, which opens the user's default system editor.
    *   **Rationale:** Greatly improves the user experience for writing detailed or lengthy prompts.

## 5. Dependencies & Setup

*   **Key Libraries:**
    *   `inquirer`: ^8.2.4
*   **Setup:**
    ```bash
    npm install
    ```
*   **Run:**
    ```bash
    node src/main.js
    ```

## 6. License Information

This project is licensed under the MIT License. See the `LICENSE` file for details.
