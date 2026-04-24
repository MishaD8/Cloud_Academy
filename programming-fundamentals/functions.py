import boto3
import random
import sys
from botocore.exceptions import ClientError

def generate_bucket_name(project_name: str) -> str:
    """Generate a valid, unique S3 bucket name. """
    suffix = random.randint(1000,9999)
    # Sanitize: lowercase, replace spaces with hyphens
    clean_name = project_name.lower().replace(" ", "-")
    return f"{clean_name}-bucket-{suffix}"

def create_s3_bucket(bucket_name: str, region: str = "us-east-1") -> bool:
    """Create an S3 bucket. Returns True on success."""
    s3 = boto3.client("s3", region_name=region)

    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket created: {bucket_name}")
        return True

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "BucketAlreadyOwnedByYou":
            print(f"Bucket already exists and Mischa own it: {bucket_name}")
        elif error_code == "BucketAlreadyExists":
            print(f"Name taken globally - try again: {bucket_name}")
        else:
            print(f"AWS error [{error_code}]: {e}")
        return False

def main():
    bucket_name = generate_bucket_name("s3april24")
    print(f"Attempting to create: {bucket_name}")
    success = create_s3_bucket(bucket_name)
    if not success:
        sys.exit(1)

if __name__=="__main__":
    main()

