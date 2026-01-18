# transform the AWS Technical Assistant into a specialized agent for a completely different domain

import os
from strands import Agent
from strands.models import BedrockModel

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

# TODO: Change this system prompt to create a specialized agent for a different domain
system_prompt = "You are a great story teller. Provide highly creative and descriptive context regarding the given topics"

# Create an agent with the Bedrock model and AWS Technical Assistant system prompt
agent = Agent(
    model=model,
    system_prompt=system_prompt
)

# TODO: Update this query to match your new specialized domain
agent("How would you make the role of Ginny right in the Harry Potter movies?")