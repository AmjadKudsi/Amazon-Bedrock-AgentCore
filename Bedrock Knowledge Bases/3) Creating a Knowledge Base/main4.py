# Extract the knowledge base ID from the creation response and print it
# Use that ID to check the current status with another API call
#Extract and print the status to monitor your knowledge base

import os
import uuid
import boto3

# Create Bedrock Agent client
bedrock_agent_client = boto3.client("bedrock-agent")

# Get AWS account ID and region using STS and environment
sts_client = boto3.client("sts")
account_id = sts_client.get_caller_identity()["Account"]

# AWS region name
REGION_NAME = os.getenv("AWS_REGION", "us-east-1")

# Name of the S3 Vectors index
VECTOR_INDEX_NAME = "bedrock-vector-index"

# Build the S3 Vectors index ARN as a constant
vector_index_arn = f"arn:aws:s3vectors:{REGION_NAME}:{account_id}:bucket/bedrock-vector-bucket/index/{VECTOR_INDEX_NAME}"

# Create a unique knowledge base name
KB_NAME = "bedrock-knowledge-base"

# IAM role ARN for knowledge base permissions
KB_ROLE_ARN = f"arn:aws:iam::{account_id}:role/kb-service-role"

# Set the embedding model ID to use
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

# Set the number of dimensions for the embeddings
EMBEDDING_DIMENSIONS = 1024

try:
    # Create Bedrock Knowledge Base
    kb_response = bedrock_agent_client.create_knowledge_base(
        name=KB_NAME,
        description="Knowledge base using S3 Vectors for document retrieval",
        roleArn=KB_ROLE_ARN,
        knowledgeBaseConfiguration={
            "type": "VECTOR",
            "vectorKnowledgeBaseConfiguration": {
                "embeddingModelArn": (
                    f"arn:aws:bedrock:{REGION_NAME}::foundation-model/{EMBEDDING_MODEL_ID}"
                ),
                "embeddingModelConfiguration": {
                    "bedrockEmbeddingModelConfiguration": {
                        "dimensions": EMBEDDING_DIMENSIONS
                    }
                },
            },
        },
        storageConfiguration={
            "type": "S3_VECTORS",
            "s3VectorsConfiguration": {
                "indexArn": vector_index_arn,
            },
        },
        clientToken=str(uuid.uuid4()),  # Unique client token for idempotency
    )

    # TODO: Extract the Knowledge Base ID from the response and print it
    knowledge_base_id = kb_response["knowledgeBase"]["knowledgeBaseId"]
    print(f"Knowledge Base ID: {knowledge_base_id}")

    # TODO: Use the knowledge base ID to check its status with get_knowledge_base()
    kb_status = bedrock_agent_client.get_knowledge_base(
        knowledgeBaseId=knowledge_base_id
    )

    # TODO: Extract and print the current status from the status response
    status = kb_status["knowledgeBase"]["status"]
    print(f"Knowledge Base Status: {status}")

except Exception as e:
    print(f"Error: {e}")