# complete three key components BedrockModel instance, an appropriate system prompt and initialize an Agent

import os
from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator, retrieve

# Define the Bedrock model ID
model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Read guardrail info from environment variables
guardrail_id = os.getenv("GUARDRAIL_ID")
guardrail_version = os.getenv("GUARDRAIL_VERSION", "DRAFT")

# Read knowledge base and region from environment variables
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID")
REGION = os.getenv("AWS_REGION")

# TODO: Create a Bedrock model with guardrail configuration
# Use model_id, guardrail_id, and guardrail_version parameters
model = BedrockModel(
    model_id=model_id,
    guardrail_id=guardrail_id,
    guardrail_version=guardrail_version
)

# TODO: Define the system prompt for AWS Technical Assistant
# The prompt should identify the agent as an AWS Technical Assistant
system_prompt = "You are an AWS Technical Assistant. Provide clear, accurate information about AWS services."


# TODO: Create an agent with both calculator and retrieve tools
# Use the model, system_prompt, and tools parameters
agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[calculator, retrieve]
)