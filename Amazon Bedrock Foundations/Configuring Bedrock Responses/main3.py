// configure two different token limits for the same AWS Lambda query

import boto3

# Create a Bedrock Runtime client
client = boto3.client("bedrock-runtime")

# Define the model ID
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Define the system prompt that sets the AI's role and behavior
system_prompt = "You are an AWS Technical Assistant. Provide clear, accurate information about AWS services."

# Create the user message asking about AWS Lambda
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": "Explain AWS Lambda and its key benefits for developers."
            }
        ],
    },
]

try:
    print("=== BRIEF SUMMARY (128 tokens) ===")
    # TODO: Set maxTokens to 128 for a brief summary
    response_brief = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        system=[{"text": system_prompt}],
        inferenceConfig={
            "maxTokens": 128,   
            "temperature": 0.2,
            "topP": 0.9,
        },
    )

    # Extract and print brief response
    output_message = response_brief.get("output", {}).get("message", {})
    parts = output_message.get("content", [])
    text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
    brief_response = "".join(text_chunks).strip()
    print(brief_response)
    
    print("\n=== DETAILED EXPLANATION (512 tokens) ===")
    # TODO: Set maxTokens to 512 for a detailed explanation
    response_detailed = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        system=[{"text": system_prompt}],
        inferenceConfig={
            "maxTokens": 512,  
            "temperature": 0.2,
            "topP": 0.9,
        },
    )

    # Extract and print detailed response
    output_message = response_detailed.get("output", {}).get("message", {})
    parts = output_message.get("content", [])
    text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
    detailed_response = "".join(text_chunks).strip()
    print(detailed_response)
    
except Exception as e:
    print(f"Error: {e}")