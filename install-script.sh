#!/bin/bash

# Hardcoded GitHub repository URL
GITHUB_URL="https://github.com/bboynton97/EvilGPT.git"

# Clone the repository
git clone "$GITHUB_URL" project
cd project || { echo "Failed to enter the project directory"; exit 1; }

# Set environment variables
export AGENTOPS_API_KEY="value1"
export OPENAI_API_KEY="value2"
export FTP_PASSWORD="value2"

# Install dependencies using pip 
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
else
  echo "No requirements.txt found. Skipping dependency installation."
fi

# Run the main script
python src/main.py
