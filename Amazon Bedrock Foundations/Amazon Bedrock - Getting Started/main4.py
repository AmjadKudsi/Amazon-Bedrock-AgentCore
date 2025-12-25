// complete the response parsing logic in the provided code

import boto3

# Create a Bedrock Runtime client with your default region (us-east-1)
client = boto3.client("bedrock-runtime")

# Define a Bedrock model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Create the user message asking for AWS compute recommendations
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": (
                    "Explain to a beginner what is AWS Bedrock."
                )
            }
        ],
    },
]

try:
    # Call Bedrock model using the converse method
    response = client.converse(
        modelId=MODEL_ID,
        messages=messages
    )

    # TODO: Extract the output message from the response
    output_message = response.get("output", {}).get("message", {})
    # TODO: Get the content parts from the message
    parts = output_message.get("content", [])
    # TODO: Extract text from each content part and join them
    text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
    # TODO: Print the AI's response
    full_response = "".join(text_chunks).strip()
    print(full_response)
    
except Exception as e:
    print(f"Error: {e}")