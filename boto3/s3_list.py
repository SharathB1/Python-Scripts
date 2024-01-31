import boto3

def list_s3_buckets():
    """ List all S3 buckets in the AWS account """
    s3 = boto3.client('s3')

    try:
        response = s3.list_buckets()
        if response['Buckets']:
            print("S3 Buckets in your AWS Account:")
            for bucket in response['Buckets']:
                print(f"- {bucket['Name']}")
        else:
            print("No S3 buckets found.")
    except Exception as e:
        print(f"Error retrieving S3 buckets: {e}")

if __name__ == "__main__":
    list_s3_buckets()
