// transform the AI assistant from giving focused technical answers to being more creative for brainstorming scenarios

import boto3

# Create a Bedrock Runtime client
client = boto3.client("bedrock-runtime")

# Define the model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Define the system prompt that sets the AI's role and behavior
system_prompt = "You are an AWS Technical Assistant. Provide clear, accurate information about AWS services."

# TODO: Update the user message to ask for creative AWS architecture ideas
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": (
                    "Explain AWS architecture with reference to popular movies, as explaining to a non-technical person"
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
            # TODO: Increase temperature to 0.7 for more creative responses
            "temperature": 0.7,  # Low temperature for more focused responses
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