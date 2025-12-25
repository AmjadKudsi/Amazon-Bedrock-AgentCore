#!/bin/bash

cd /usercode/FILESYSTEM

# Check if setup is complete
if [ ! -f "/tmp/.setup_finished" ]; then
    echo "The setup is not finished yet. Try again in a few seconds." >&2
    exit 1
fi

# Run code
python main.py