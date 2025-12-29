# create the full vector storage infrastructure setup that combines client initialization, bucket creation, index creation, and information retrieval

import boto3

# Create S3 Vectors client
s3_vectors_client = boto3.client("s3vectors")

# Create a unique vector bucket name
VECTOR_BUCKET_NAME = "bedrock-vector-bucket"

# Create a unique vector index name
VECTOR_INDEX_NAME = "bedrock-vector-index"

# Set the embedding dimensions
EMBEDDING_DIMENSIONS = 1024

# Create an S3 vector bucket for embeddings storage
s3_vectors_client.create_vector_bucket(vectorBucketName=VECTOR_BUCKET_NAME)

# Create a vector index
s3_vectors_client.create_index(
    vectorBucketName=VECTOR_BUCKET_NAME,
    indexName=VECTOR_INDEX_NAME,   
    dimension=EMBEDDING_DIMENSIONS,
    distanceMetric="cosine",
    dataType="float32",
)

# List the vector indexes in the bucket
indexes_response = s3_vectors_client.list_indexes(
    vectorBucketName=VECTOR_BUCKET_NAME
)

# Get the vector index ARN
index_arn = indexes_response["indexes"][0]["indexArn"]

# Print the vector index ARN
print(f"Vector Index ARN: {index_arn}")