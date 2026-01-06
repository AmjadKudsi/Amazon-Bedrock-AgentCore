// insert these prepared vectors into the S3 vector index

import json
import boto3

from utils import load_documents_from_folder

# Create AWS clients for S3 Vectors and Bedrock Runtime
s3_vectors_client = boto3.client("s3vectors")
bedrock_runtime_client = boto3.client("bedrock-runtime")

# Names for the existing vector bucket and index
VECTOR_BUCKET_NAME = "bedrock-vector-bucket"
VECTOR_INDEX_NAME = "bedrock-vector-index"

# Set the embedding model ID to use
EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v2:0"

# Set the number of dimensions for the embeddings
EMBEDDING_DIMENSIONS = 1024

# Load documents from folder
documents = load_documents_from_folder("docs/")

try:
    # Create a list to store the vectors to insert
    vectors_to_insert = []
    
    # Generate embeddings for each document
    for doc in documents:
        print(f"Processing: {doc['key']}")
        
        # Create embedding request
        embedding_request = {
            "inputText": doc["content"],         # The text content of the document to embed
            "dimensions": EMBEDDING_DIMENSIONS,  # Number of dimensions for the embedding vector
            "normalize": True,                   # Normalize the embedding vector (recommended for similarity search)
        }
        # Get embedding from Bedrock
        response = bedrock_runtime_client.invoke_model(
            modelId=EMBEDDING_MODEL_ID, 
            body=json.dumps(embedding_request)
        )

        # Load the response body
        response_body = json.loads(response["body"].read())

        # Get the embedding from the response body
        embedding = response_body["embedding"]

        # Prepare the vector for insertion
        vectors_to_insert.append({
            "key": doc["key"],  # Unique identifier for the vector (from filename)
            "data": {
                "float32": [float(x) for x in embedding]  # Embedding vector as list of float32 values
            },
            "metadata": {
                "AMAZON_BEDROCK_TEXT": doc["content"],
                "x-amz-bedrock-kb-source-uri": doc["metadata"].get("filename", doc["key"]),
                **doc["metadata"],
            },
        })

    # TODO: Insert vectors into S3 Vectors index using the put vectors operation
    s3_vectors_client.put_vectors(
        vectorBucketName=VECTOR_BUCKET_NAME,
        indexName=VECTOR_INDEX_NAME,
        vectors=vectors_to_insert
    )

    # Print the number of documents uploaded
    print(f"Successfully uploaded {len(vectors_to_insert)} documents!")

except Exception as e:
    print(f"Error: {e}")