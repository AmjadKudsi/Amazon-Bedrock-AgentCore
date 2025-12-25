#!/bin/sh
# This script will be run when the environment is initialized.
# Add any setup logic here.

echo "Setting up environment..."

# File with credentials
JSON_FILE=".setup/aws-credentials.json"

# Pull the credential values from aws-credentials.json
read -r ACCESS_KEY_ID SECRET_ACCESS_KEY < <(
python - <<'PY' "$JSON_FILE"
import json, sys
d = json.load(open(sys.argv[1]))
print(d["accessKeyId"], d["secretAccessKey"])
PY
)

# Configure AWS credentials
aws configure set default.region us-east-1
aws configure set aws_access_key_id ${ACCESS_KEY_ID}
aws configure set aws_secret_access_key ${SECRET_ACCESS_KEY}

# Execute extra setup steps
bash .setup/setup_steps.sh > /dev/null 2>&1

# Create a temporary file to mark that setup has successfully completed
touch /tmp/.setup_finished

# Notify the user
echo "Setup complete!"