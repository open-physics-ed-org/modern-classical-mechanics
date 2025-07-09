#!/bin/bash
# Setup script for modern-classical-mechanics project
# Creates a Python virtual environment in .venv and installs dependencies

set -e

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

echo "Environment setup complete. To activate, run: source .venv/bin/activate"
