#!/bin/bash

# Change to the specified directory
cd /home/ubuntu/EvilGPT || exit

# Activate the Python virtual environment
source env/bin/activate

# Run the main.py script
python src/main.py
