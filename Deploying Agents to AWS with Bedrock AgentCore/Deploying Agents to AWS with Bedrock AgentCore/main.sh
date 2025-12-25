#!/bin/bash

cd /usercode/FILESYSTEM

if [ ! -f "/tmp/.setup_finished" ]; then
    echo "The setup is not finished yet. Try again in a few seconds." >&2
    exit 1
fi

# If questions.json exists run the quiz's format answers
if [ -f .codesignal/questions.json ]; then
    cd .codesignal/learn_quiz-task
    curl -X POST localhost:3000/validate &> /dev/null
    python format_answers.py

    exit 0
fi

# Path of the file with the run configuration
RUN_CONFIG_FILE=".codesignal/run_config.json"

# Read JSON
JSON_CONTENT="$(cat "$RUN_CONFIG_FILE")"

# Validate JSON
if ! echo "$JSON_CONTENT" | jq empty >/dev/null 2>&1; then
    echo "Invalid JSON in $RUN_CONFIG_FILE" >&2
    exit 1
fi

# Extract flags with safe defaults
COMMANDS="$(echo "$JSON_CONTENT" | jq -r '.commands // false')"
TEST="$(echo "$JSON_CONTENT" | jq -r '.test // false')"
SOLUTION="$(echo "$JSON_CONTENT" | jq -r '.solution // false')"

# 1) Print commands ONLY if commands == true
if [ "$COMMANDS" = "true" ]; then
    bash .codesignal/run_check.sh
fi

# 2) Activate venv
source /bootstrap-apps/.virtualenvs/aws-agents/bin/activate

# 3) Run tests ONLY if test == true
if [ "$TEST" = "true" ]; then
    echo "Running tests:"
    bash .codesignal/run_test.sh
fi

# 4) Run solution ONLY if solution == true AND both others are false
if [ "$SOLUTION" = "true" ] && [ "$COMMANDS" != "true" ] && [ "$TEST" != "true" ]; then
   bash .codesignal/run_solution.sh
fi