#!/bin/bash

# Change to the specified directory
cd /home/ubuntu/EvilGPT || exit

# Activate the Python virtual environment
source venv/bin/activate

# Run the main.py script
python src/main.py
