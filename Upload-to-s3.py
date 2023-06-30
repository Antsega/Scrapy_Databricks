# Databricks notebook source
# Cell 1: Import required packages
import os
import boto3
import .env.local
# Cell 2: Load environment variables
dbutils.secrets.mount('<secret-scope-name>', '<mount-point>')


# Cell 3: Initialize S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
bucket_name = os.getenv("S3_BUCKET_NAME")

# Cell 4: Upload files to S3
# Set the local directory where the files are stored
local_directory = "/tmp"

# Iterate over the files in the directory
for root, dirs, files in os.walk(local_directory):
    for filename in files:
        # Determine full local filepath
        local_path = os.path.join(root, filename)
        
        # Format S3 key (This assumes that the S3 key should mimic the local path.)
        # Change this line if the S3 key should be structured differently.
        s3_key = local_path.lstrip("/")
        
        # Check if file is .json or .pdf
        _, ext = os.path.splitext(filename)
        if ext in [".json", ".pdf"]:
            # Open the file in read mode and upload to S3
            with open(local_path, 'rb') as data:
                s3.upload_fileobj(data, bucket_name, s3_key)


# COMMAND ----------


