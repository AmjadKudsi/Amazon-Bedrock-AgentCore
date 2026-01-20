# assemble all the components you've learned about into one working system

import os
from strands import Agent
from strands.models import BedrockModel

# Define the Bedrock model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Read guardrail info from environment variables
GUARDRAIL_ID = os.getenv("GUARDRAIL_ID")
GUARDRAIL_VERSION = os.getenv("GUARDRAIL_VERSION", "DRAFT")

# TODO: Create a Bedrock model with guardrail configuration
model = BedrockModel(
    model_id=MODEL_ID,
    guardrail_id=GUARDRAIL_ID,
    guardrail_version=GUARDRAIL_VERSION
)

# TODO: Define the system prompt for a Creative Writing Agent
system_prompt = "You are an AWS Technical Assistant. Provide clear, accurate information about AWS services."

# TODO: Create an agent with the Bedrock model and system prompt
agent = Agent(
    model=model,
    system_prompt=system_prompt
)

# TODO: Send your first message asking for help developing a story character
agent("Explain to a beginner the pros and cons of AWS Bedrock")