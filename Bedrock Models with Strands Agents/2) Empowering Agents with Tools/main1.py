# enable mathematical operations for calculator tool

import os
from strands import Agent
from strands.models import BedrockModel
# TODO: Import the calculator tool from strands_tools
from strands_tools import calculator

# Define the Bedrock model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Read guardrail info from environment variables
GUARDRAIL_ID = os.getenv("GUARDRAIL_ID")
GUARDRAIL_VERSION = os.getenv("GUARDRAIL_VERSION", "DRAFT")

# Create a Bedrock model with guardrail configuration
model = BedrockModel(
    model_id=MODEL_ID,
    guardrail_id=GUARDRAIL_ID,
    guardrail_version=GUARDRAIL_VERSION
)

# Define the system prompt for AWS Technical Assistant
system_prompt = "You are an AWS Technical Assistant. Provide clear, accurate information about AWS services."

# Create an agent with calculator tool
agent = Agent(
    model=model,
    system_prompt=system_prompt,
    # TODO: Pass the calculator tool to the agent
    tools=[calculator]
)

# Send your first message to the agent asking about storage calculations
agent("I need to store 2.5 TB of data. How many GB is that?")