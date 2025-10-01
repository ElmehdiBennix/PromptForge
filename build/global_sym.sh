#!/bin/sh

# This script sets up global symbolic links for the PromptForge project.
# It ensures that the 'gema' command is available globally.
# Usage: Run this script from the root of the PromptForge project.
# Make sure you have the necessary permissions to create symbolic links.

npm install

sudo npm link

echo "Global symbolic link for 'gema' has been created."
