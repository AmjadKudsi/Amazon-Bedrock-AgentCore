// convert a general AWS assistant into a specialized security expert

import boto3

# Create a Bedrock Runtime client
client = boto3.client("bedrock-runtime")

# Define the model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# TODO: Change this system prompt to make the AI an "AWS Security Expert"
# Define the system prompt that sets the AI's role and behavior
system_prompt = "You are an AWS Security Expert. Provide clear, accurate information regarding industrial standard security practices."

# TODO: Update the user message to ask about VPC security best practices
# Create the user message asking about model configuration parameters
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": (
                    "Explain the significance of Virtual Private Cloud (VPC) and its best practices"
                )
            }
        ],
    },
]

try:
    # Call Bedrock model with configurable inference parameters
    response = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        system=[{"text": system_prompt}],
        inferenceConfig={
            "maxTokens": 256,    # Limit response to 256 tokens
            "temperature": 0.2,  # Low temperature for more focused responses
            "topP": 0.9,         # Top-p sampling for response diversity
        },
    )

    # Extract and combine text content from the Bedrock response
    output_message = response.get("output", {}).get("message", {})
    parts = output_message.get("content", [])
    text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
    full_response = "".join(text_chunks).strip()

    # Print the AI's response
    print(full_response)
    
except Exception as e:
    print(f"Error: {e}")