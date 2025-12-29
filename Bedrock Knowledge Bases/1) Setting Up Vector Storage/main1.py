# complete the provided code by implementing the missing pieces needed to establish a basic vector storage setup

import boto3

# TODO: Create S3 Vectors client
s3_vectors_client = boto3.client("s3vectors")

# Create a unique vector bucket name
VECTOR_BUCKET_NAME = "bedrock-vector-bucket"

# TODO: Create an S3 vector bucket for embeddings storage
VECTOR_INDEX_NAME = "bedrock-vector-index"

s3_vectors_client.create_vector_bucket(vectorBucketName=VECTOR_BUCKET_NAME)

print("Vector bucket created successfully!")