import boto3
from botocore.exceptions import ClientError

def delete_empty_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    for bucket in buckets:
        try:
            # List objects in the bucket
            objects = s3.list_objects_v2(Bucket=bucket['Name'], MaxKeys=1)
            
            # Check if the bucket is empty
            if 'Contents' not in objects:
                # Delete the bucket
                s3.delete_bucket(Bucket=bucket['Name'])
                print(f"Deleted empty bucket: {bucket['Name']}")
            else:
                print(f"Bucket {bucket['Name']} is not empty.")
        except ClientError as e:
            print(f"Error processing bucket {bucket['Name']}: {e}")

if __name__ == "__main__":
    delete_empty_buckets()

