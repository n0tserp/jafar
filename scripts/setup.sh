#!/bin/bash

# Jafar Setup Script — Works on macOS (Intel + Apple Silicon)
# Uses Python 3.12 via Homebrew + virtual environment

set -e  # Exit on any error

echo "Setting up Jafar..."

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Install Python 3.12
echo "Installing Python 3.12..."
brew install python@3.12 || true

# Create virtual environment
echo "Creating virtual environment..."
/usr/local/opt/python@3.12/bin/python3.12 -m venv .venv

# Activate venv
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install spacy + model
echo "Installing spaCy..."
pip install spacy==3.7.2
python -m spacy download en_core_web_sm

# Install pendulum with pre-built wheel
echo "Installing pendulum (ARM64-safe)..."
pip install "pendulum==3.1.0" --only-binary=:all: --no-cache-dir

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt --no-cache-dir

# Install Prefect
echo "Installing Prefect..."
pip install prefect==2.14.5

# Setup Prefect
echo "Setting up Prefect..."
prefect profile create default || true

echo ""
echo "Setup complete!"
echo "Next: source .venv/bin/activate && docker-compose up --build"
echo "Dashboard: http://localhost:8501"