# Your provided code has the calculator tool, Create your own custom pricing tool, with an agent and a simple query 

import os
import json
from strands import Agent, tool
from strands.models import BedrockModel
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

# AWS pricing information (provided for you)
aws_pricing_data = [
    {
        "service": "S3",
        "pricing": {
            "standard_storage_per_gb_month": 0.023,
            "requests_per_1000_get": 0.0004,
            "requests_per_1000_put": 0.005
        },
        "free_tier": {
            "storage_gb": 5,
            "get_requests": 20000,
            "put_requests": 2000
        }
    },
    {
        "service": "EC2",
        "pricing": {
            "t2_micro_per_hour": 0.0116,
            "t3_small_per_hour": 0.0208,
            "t3_medium_per_hour": 0.0416
        },
        "free_tier": {
            "t2_micro_hours": 750
        }
    }
]

# TODO: Create a custom tool using the @tool decorator that returns the pricing information
# Remember to include a docstring explaining what the tool does
@tool
def aws_pricing(service: str | None = None) -> str:
    """
    Return the provided AWS pricing and free tier information for S3 and EC2.
    If `service` is provided (for example, "S3" or "EC2"), only that service is returned.
    """
    if service:
        filtered = [
            item for item in aws_pricing_data
            if item.get("service", "").lower() == service.lower()
        ]
        return json.dumps(filtered, indent=2)
    return json.dumps(aws_pricing_data, indent=2)

# TODO: Create an agent with both the calculator and your new pricing tool
agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[calculator, aws_pricing]
)

# TODO: Write a query that requires both the calculator and your pricing tool working together
# Hint: think about storage costs, EC2 runtime costs, or cost comparisons that need calculations
agent("Using the aws_pricing tool, calculate the total monthly cost for S3 Standard storage of 50 GB for 1 month plus 30000 GET requests and 5000 PUT requests after applying the S3 free tier, then add the cost of running one EC2 t3.small instance for 100 hours, and use the calculator tool for all arithmetic to return the final total in USD.")