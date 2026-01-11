# integrate the entire Knowledge Base creation workflow by filling in the missing components in the provided code

import os
import uuid
import boto3

# Create Bedrock Agent client
bedrock_agent_client = boto3.client("bedrock-agent")

# TODO: Add STS client and get AWS account ID
sts_client = boto3.client("sts")
account_id = sts_client.get_caller_identity()["Account"]

# AWS region name
REGION_NAME = os.getenv("AWS_REGION", "us-east-1")

# TODO: Add the S3 Vectors index name constant
VECTOR_INDEX_NAME = "bedrock-vector-index"

# TODO: Build the S3 Vectors index ARN using account_id
vector_index_arn = f"arn:aws:s3vectors:{REGION_NAME}:{account_id}:bucket/bedrock-vector-bucket/index/{VECTOR_INDEX_NAME}"

# Create a unique knowledge base name
KB_NAME = "bedrock-knowledge-base"

# TODO: Add IAM role ARN for knowledge base permissions
KB_ROLE_ARN = f"arn:aws:iam::{account_id}:role/kb-service-role"

# Set the embedding model ID to use
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

# TODO: Add the number of dimensions for the embeddings
EMBEDDING_DIMENSIONS = 1024

try:
    # TODO: Complete the create_knowledge_base call with all required parameters
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
        clientToken=str(uuid.uuid4()),  
    )

    # TODO: Extract the Knowledge Base ID from the response and print it
    knowledge_base_id = kb_response["knowledgeBase"]["knowledgeBaseId"]
    print(f"Knowledge Base ID: {knowledge_base_id}")

    # TODO: Check the status of the newly created Knowledge Base and print the status
    kb_status = bedrock_agent_client.get_knowledge_base(
        knowledgeBaseId=knowledge_base_id
    )
    
    status = kb_status["knowledgeBase"]["status"]
    print(f"Knowledge Base Status: {status}")

except Exception as e:
    print(f"Error: {e}")